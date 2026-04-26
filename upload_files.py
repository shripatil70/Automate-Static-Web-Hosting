import boto3

s3 = boto3.client("s3")

def upload_file(bucket_name):
    s3.upload_file(
        Filename="website/index.html",
        Bucket=bucket_name,
        Key="index.html",
        ExtraArgs={'ContentType': 'text/html'}
    )
    print("File uploaded")