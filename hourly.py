import json
from healthcheck import healthcheck

def hourly(event, context):
    body = {
    }

    body['healthcheck']=healthcheck()

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
