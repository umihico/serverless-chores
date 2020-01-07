import json
import slack
from healthcheck import healthcheck
import pprint

def minutely(event, context):
    body = {
    }

    body['healthcheck']=healthcheck()
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
