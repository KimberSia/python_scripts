#search buckets 
import boto3

resource = boto3.resource("s3")

# obtain the number of buckets 
bucket_list = list(resource.buckets.all())
print(len(bucket_list))

#list of buckets
for bucket in resource.buckets.all():
    print(bucket.name)