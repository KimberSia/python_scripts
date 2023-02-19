#create multiple instances 


import boto3
ec2_resource=boto3.resource("ec2")


ec2_resource.create_instances(ImageId='ami-0dfcb1ef8550277af',
   InstanceType='t2.micro',
   MaxCount=3,
   MinCount=2)


