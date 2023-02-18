#upload file to bucket
import boto3

s3_resource = boto3.client("s3")

# Upload multiple files to S3 bucket
s3_resource.upload_file(
    Filename = "README.md", # Existing file in  CWD 
    Bucket = "5b1988ae-af9c-11ed-b434-325096b39f47", # Name of bucket 
    Key = "uploadtest2.png") # This will be the new name of the file in the bucket

import os
import glob

cwd=os.getcwd() # Gets current working directory
cwd=cwd+ "/upload"
print(cwd)

files=glob.glob(cwd+"*.py")
print(files)



for file in files:
    s3_resource = boto3.client("s3")
    s3_resource.upload_file(
        Filename= file,
        Bucket="5b1988ae-af9c-11ed-b434-325096b39f47",
        Key=file.split("/")[-1])