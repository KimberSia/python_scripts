import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("3a1b9398-af9e-11ed-beb7-325096b39f47")
response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint':'us-east-2'
        },
        
)

print(response)