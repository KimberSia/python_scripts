#how to get a creation date 
import boto3

s3_resource = boto3.client("s3")
print(s3_resource)


print(s3_resource.list_buckets()["Buckets"][0]["Name"])


creation_date = s3_resource.list_buckets()["Buckets"][0]["CreationDate"]
creation_date.strftime("%d%m%y_%H:%M:%s")
print(creation_date)



#create name and date 
for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])