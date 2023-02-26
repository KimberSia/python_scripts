import json
import boto3
from datetime import datetime
from datetime import timedelta #time delta is used for us to bring our time to our current timezone


def lambda_handler(event, context):
    now = datetime.now() - timedelta(hours=5)# current timezone displayed by indicating the difference in hours between EST and UTC
    current_time=now.strftime("%m/%d/%Y, %H:%M:%S %p") #displays human readable M/D/Y and H:M:S 
     
    
    sqs = boto3.client('sqs') #service resource
    sqs.send_message( #where we are sending message to 
        QueueUrl = 'https://sqs.us-east-1.amazonaws.com/228758456094/ProjectWeek15',
        MessageBody = current_time)

    return {
        'statusCode': 200,
        'body': json.dumps(current_time)#input display