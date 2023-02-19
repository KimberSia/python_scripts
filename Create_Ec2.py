#create and launch EC2 instance 

import boto3

ec2_resource = boto3.resource("ec2")

ec2_resource.create_instances(ImageId = "ami-0dfcb1ef8550277af", #ami can be found by opening up launch instance 
InstanceType = "t2.micro", MaxCount = 1, MinCount = 1)
