#obtain ec2 instance id

import boto3

ec2 = boto3.client("ec2")
x = ec2.describe_instances()

x.keys()
len(x["Reservations"])


data = x["Reservations"][0]
data_instance = data["Instances"]

for i in range(len(data_instance)):
    print(data_instance[i])