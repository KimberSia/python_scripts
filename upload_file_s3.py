#upload file to bucket

import boto3


s3_resource = boto3.client("s3")

s3_resource.upload_file(
    Filename = "README.md", #file from directory
    Bucket = "5b1988ae-af9c-11ed-b434-325096b39f47", #where you want the file to go 
    Key = "week 9 watermark.png") #name of the file 
    
