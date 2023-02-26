#create sqs queue for boto3

import boto3 

#service resource
sqs_client = boto3.client("sqs")


#create the queue
response = sqs_client.create_queue(
        QueueName ='ProjectWeek15'
      
    )
#prints the queue url along additional information    
print(response)

