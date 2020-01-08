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

def test_minutely():
    assert minutely(None, None)['statusCode']==200

if __name__ == '__main__':
    test_minutely()
