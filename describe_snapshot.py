#describe ebs volume

import boto3
ec2_boto3=boto3.client("ec2")


ec2_boto3.describe_snapshots(SnapshotIds=[
    'snap-01a69e3fa11be2b09'
    ])
