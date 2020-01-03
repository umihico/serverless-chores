import json
import slack
from healthcheck import healthcheck
from portscan import portscan
import pprint

def hourly(event, context):
    body = {
    }

    body['healthcheck']=healthcheck()
    body['portscan']=portscan()

    slack.log(pprint.pformat(body))
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
