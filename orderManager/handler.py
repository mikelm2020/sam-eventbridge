import boto3
import json

eventbridge = boto3.client('events')

def put_event_in_eventbridge(order_details):
    detail = { 
        'restaurantName': order_details['restaurantName'],
        'order': order_details['order'],
        'customerName': order_details['customerName'],
        'amount': order_details['amount']
    }

    params = {
        'Entries': [
            {
                'Detail': json.dumps(detail),
                'DetailType': 'order',
                'Source': 'custom.orderManager'
            }
        ]
    }

    print(params)
    return eventbridge.put_events(Entries=params['Entries'])

def put_order(event, context):
    print('putOrder')

    order_details = json.loads(event['body'])
    data = put_event_in_eventbridge(order_details)

    print(data)

    return {
        'statusCode': 200,
        'body': json.dumps(order_details),
        'headers': {}
    }
