#delete aws ebs volume snapshot


import boto3

ec2_client= boto3.client("ec2")


ec2_client.delete_VolumeId(VolumeId='vol-0037c9d85bc49d3e3')