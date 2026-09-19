import boto3

kw = dict(endpoint_url="http://localhost:4566", region_name="us-east-1",
          aws_access_key_id="test", aws_secret_access_key="test")

s3 = boto3.client("s3", **kw)
ec2 = boto3.client("ec2", **kw)

def seed():
    s3.create_bucket(Bucket="bad-public-bucket")
    s3.put_bucket_acl(Bucket="bad-public-bucket", ACL="public-read")

    s3.create_bucket(Bucket="good-private-bucket")
    s3.put_public_access_block(
        Bucket="good-private-bucket",
        PublicAccessBlockConfiguration={
            "BlockPublicAcls": True,
            "IgnorePublicAcls": True,
            "BlockPublicPolicy": True,
            "RestrictPublicBuckets": True,
        })

    sg = ec2.create_security_group(GroupName="worst-sg", Description="all traffic open")
    ec2.authorize_security_group_ingress(
        GroupId=sg["GroupId"], 
        IpPermissions=[{
            "IpProtocol": "-1",
            "IpRanges": [{"CidrIp": "0.0.0.0/0"}]}])

    sg = ec2.create_security_group(GroupName="web-sg", Description="public https")
    ec2.authorize_security_group_ingress(
        GroupId=sg["GroupId"], 
        IpProtocol="tcp",
        FromPort=443,
        ToPort=443,
        CidrIp="0.0.0.0/0")

    for name, cidr in [("bad-sg", "0.0.0.0/0"), ("good-sg", "10.0.0.0/16")]:
        sg = ec2.create_security_group(GroupName=name, Description=name)
        ec2.authorize_security_group_ingress(
            GroupId=sg["GroupId"], 
            IpProtocol="tcp",
            FromPort=22,
            ToPort=22,
            CidrIp=cidr)
if __name__ == "__main__":
    print("seeded") 
