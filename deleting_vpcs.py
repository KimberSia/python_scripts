#removing vpcs 

import boto3


client=boto3.client("ec2")

response = client.delete_vpc(
    VpcId='vpc-061905b181e0cab9b', 
    
    )
print(response)