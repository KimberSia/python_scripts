
#stopping ec2 instances
import boto3
ec2_resource=boto3.resource("ec2")

#input instance id's obtained from ec2 console
ec2_resource.Instance('i-0d5da7d084b4ddf64').stop()
ec2_resource.Instance('i-0c0a972270353ab98').stop()
ec2_resource.Instance('i-05a149fd1aa7682ed').stop()


