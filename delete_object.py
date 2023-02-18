#deleting objects 

import boto3

s3_resource=boto3.client("s3")
#delete single object
s3_resource.delete_object(Bucket='5b1988ae-af9c-11ed-b434-325096b39f47',
    Key='uploadtest2.png')
