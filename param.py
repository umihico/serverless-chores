import os
import boto3

def get(key):
    return os.getenv(key, boto3.client('ssm').get_parameter(Name=key)['Parameter']['Value'])

def test_get():
    print(get('SLACK_TOKEN'))
    print(get('SLACK_ID'))
    print(get('SLACK_ID_DEBUG'))
    print(get('SLACK_ID_ERROR'))

if __name__ == '__main__':
    test_get()
