import json
from healthcheck import healthcheck
from portscan import portscan

def hourly(event, context):
    body = {
    }

    body['healthcheck']=healthcheck()
    body['portscan']=portscan()

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
