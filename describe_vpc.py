#describing vpc 

import boto3

client=boto3.client("ec2")
#how to describe all vpcs available in acct

x=client.describe_vpcs()
no_of_vpcs=x["Vpcs"]
len(no_of_vpcs)


for vpc in no_of_vpcs:
    print(vpc["VpcId"])
    
    
    
x=client.describe_vpcs(VpcIds=["vpc-0f9d2ec2ce9786d5b"])