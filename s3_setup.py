import boto3
from botocore.exceptions import ClientError
from config import BUCKET_NAME, REGION

s3 = boto3.client("s3")

def create_bucket():
    try:
        s3.create_bucket(
            Bucket=BUCKET_NAME,
            CreateBucketConfiguration={'LocationConstraint': REGION}
        )
        print("Bucket created:", BUCKET_NAME)
    except ClientError as e:
        print("Bucket exists or error:", e)


def enable_website():
    s3.put_bucket_website(
        Bucket=BUCKET_NAME,
        WebsiteConfiguration={
            'IndexDocument': {'Suffix': 'index.html'}
        }
    )
    print("Static website hosting enabled")


def make_bucket_public():
    policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject"],
            "Resource": [f"arn:aws:s3:::{BUCKET_NAME}/*"]
        }]
    }

    s3.put_bucket_policy(
        Bucket=BUCKET_NAME,
        Policy=str(policy).replace("'", '"')
    )
    print("Bucket made public")
    
def disable_block_public_access():
    s3.put_public_access_block(
        Bucket=BUCKET_NAME,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': False,
            'IgnorePublicAcls': False,
            'BlockPublicPolicy': False,
            'RestrictPublicBuckets': False
        }
    )
    print("Block Public Access disabled")    