import boto3

kw = dict(endpoint_url="http://localhost:4566", region_name="us-east-1",
          aws_access_key_id="test", aws_secret_access_key="test")

ADMIN_PORTS = {22,3389}
WEB_PORTS = {80,443}

def rate(permission):
    if permission.get("IpProtocol") == "-1":
        return "CRITICAL"
    lo, hi = permission.get("FromPort"), permission.get("ToPort")
    if lo is None or hi is None:
        return "HIGH"
    if any(lo <= p <= hi for p in ADMIN_PORTS):
        return "CRITICAL"
    if lo == hi and lo in WEB_PORTS:
        return "LOW"
    return "HIGH"

def check_security_groups():
    ec2 = boto3.client("ec2", **kw)
    findings = []
    for sg in ec2.describe_security_groups()["SecurityGroups"]:
        for perm in sg.get("IpPermissions", []):
            open_v4 = any(r.get("CidrIp") == "0.0.0.0/0" 
                          for r in perm.get("IpRanges", []))
            open_v6 = any(r.get("CidrIpv6") == "::/0"
                            for r in perm.get("Ipv6Ranges", []))
            if open_v4 or open_v6:
                findings.append({
                    "check_id": "SG_OPEN_INGRESS",
                    "group_id": sg["GroupId"],
                    "group_name": sg["GroupName"],
                    "protocol": perm.get("IpProtocol"),
                    "from_port": perm.get("FromPort"),
                    "to_port": perm.get("ToPort"),
                    "severity": rate(perm),
                    "reosurce_type": "security_group",
                    "resource": sg["GroupName"],
                    "reference": "CIS AWS Foundations: no 0.0.0.0/0 ingress to admin ports",
                })
    return findings

if __name__ == "__main__":
    for f in check_security_groups():
        print(f)