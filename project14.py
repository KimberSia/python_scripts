import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("8714c1f2-af9d-11ed-9e0d-325096b39f47")
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint':'us-east-2'
        },
        
)

print(response)