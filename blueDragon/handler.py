import json
import os
import boto3

# Initialize DynamoDB client using environment variables
table_name = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def blue_dragon_dlq(event, context):
    print(event)
    
    record = json.loads(event['Records'][0]['body'])
    print(record)
    
    save_item(record)

def save_item(item):
    response = table.put_item(Item=item)
    print(response)
