#deleting objects 

import boto3
import os

s3_resource = boto3.client("s3")
objects = s3_resource.list_objects(Bucket = "5b1988ae-af9c-11ed-b434-325096b39f47")["Contents"]

for object in objects:
    response = s3_resource.delete_object(Bucket = "5b1988ae-af9c-11ed-b434-325096b39f47", Key = object["Key"])