#create sqs queue for boto3

import boto3 

sqs_client = boto3.client("sqs")
response = sqs_client.create_queue(
        QueueName="ProjectWeek15"

    )
print(response)
