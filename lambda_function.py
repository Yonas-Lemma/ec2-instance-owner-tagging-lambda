
import json
import boto3

client = boto3.client('ec2')

def lambda_handler(event, context):
    # Extract username and instance ID from the event
    user = event['detail']['userIdentity']['username']
    instanceid = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']
    
    
    client.create_tags(
        Resources=[
            instanceid,  
        ],
        Tags=[
            {
                'Key': 'Owner',
                'Value': user
            },
        ]
    )
    
    return 
