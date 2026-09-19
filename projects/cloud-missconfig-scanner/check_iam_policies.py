import boto3

kw = dict(endpoint_url="http://localhost:4566", region_name="us-east-1",
          aws_access_key_id="test", aws_secret_access_key="test")

def as_list(x):
    return x if isinstance(x, list) else [x]

def check_admin_policies():
    iam = boto3.client("iam", **kw)
    findings = []
    for policy in iam.list_policies(Scope="Local")["Policies"]:
        version = iam.get_policy_version(
            PolicyArn=policy["Arn"],
            VersionId=policy["DefaultVersionId"])
        document = version["PolicyVersion"]["Document"]
        for stmt in as_list(document["Statement"]):
            if stmt.get("Effect") != "Allow":
                continue
            actions = as_list(stmt.get("Action", []))
            resources = as_list(stmt.get("Resource", []))
            if "*" in actions and "*" in resources:
                findings.append({
                    "check_id": "IAM_ADMIN_POLICY",
                    "resource_type": "iam_policy",
                    "resource": policy["PolicyName"],
                    "severity": "CRITICAL",
                    "reference": "CIS AWS Foundations: no full administrative privileges in IAM policies",
                })
                break 
    return findings
      
if __name__ == "__main__":
    for f in check_admin_policies():
        print(f)