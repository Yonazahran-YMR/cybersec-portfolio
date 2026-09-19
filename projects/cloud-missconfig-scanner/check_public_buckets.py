import logging
import boto3
from botocore.exceptions import ClientError

kw = dict(endpoint_url="http://localhost:4566", region_name="us-east-1",
          aws_access_key_id="test", aws_secret_access_key="test")

PUBLIC_URIS = {
    "http://acs.amazonaws.com/groups/global/AllUsers",
    "http://acs.amazonaws.com/groups/global/AuthenticatedUsers",
}

WRITE_PERMS = {"WRITE", "WRITE_ACP", "FULL_CONTROL"}
BLOCK_KEYS = ("BlockPublicAcls", "IgnorePublicAcls", "BlockPublicPolicy", "RestrictPublicBuckets")

def public_grant_perms(s3, name):
    acl = s3.get_bucket_acl(Bucket=name)
    return {g["Permission"] for g in acl.get("Grants", [])
            if g.get("Grantee", {}).get("URI") in PUBLIC_URIS}

def fully_blocked(s3, name):
    try:
        cfg = s3.get_public_access_block(Bucket=name)["PublicAccessBlockConfiguration"]
    except ClientError as e:
        if e.response["Error"]["Code"] == "NoSuchPublicAccessBlockConfiguration":
            return False
        raise
    return all(cfg.get(k) for k in BLOCK_KEYS)

def check_public_buckets():
    s3 = boto3.client("s3", **kw)
    findings = []
    for b in s3.list_buckets()["Buckets"]:
        name = b["Name"]
        try:
            perms = public_grant_perms(s3, name)
            blocked = fully_blocked(s3, name)
        except ClientError as e:
            logging.warning("could not assess %s: %s", name, e)
            continue

        if perms:
            severity = "CRITICAL" if perms & WRITE_PERMS else "HIGH"
            if blocked:
                severity = "LOW"
            findings.append({
                "check_id": "S3_PUBLIC_ACL",
                "resource_type": "s3_bucket",
                "resource": name,
                "permissions": sorted(perms),
                "severity": severity,
                "reference": "CIS AWS Foundations: no public S3 buckets",
            })
        if not blocked:
            findings.append({
                "check_id": "S3_NO_PUBLIC_ACCESS_BLOCK",
                "resource_type":"s3_bucket",
                "resource": name,
                "severity": "MEDIUM",
                "reference": "CIS AWS Foundations: no public S3 buckets",
            })
    return findings

if __name__ == "__main__":
    for f in check_public_buckets():
        print(f)