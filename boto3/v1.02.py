# uses s3. upload build artifacts,upload Terraform state backups, upload logs

import boto3

s3 = boto3.client('s3')

s3.upload_file(
    "app.log",
    "my-bucket",
    "logs/app.log"
)

