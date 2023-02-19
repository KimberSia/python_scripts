# CREATE A SNAPSHOT OF AN EXISTING VOLUME


import boto3

ec2_client= boto3.client("ec2")

ec2_client.create_volume(AvailabilityZone='us-east-1b',
    Encrypted=True,
    Size=12,
    SnapshotId='snap-0c8f5c07e3ecf3bae',
    VolumeType='gp2')