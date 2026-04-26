from s3_setup import create_bucket, enable_website, make_bucket_public, disable_block_public_access
from upload_files import upload_file
from config import BUCKET_NAME

def main():
    print("Starting Static Website Deployment...")

    create_bucket()
    enable_website()
    disable_block_public_access()
    make_bucket_public()
    upload_file(BUCKET_NAME)
   

    print("Deployment Complete!")

    print("\n🌐 Website URL:")
    print(f"http://{BUCKET_NAME}.s3-website-ap-south-1.amazonaws.com")

if __name__ == "__main__":
    main()