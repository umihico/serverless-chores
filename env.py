import os
import boto3
import yaml

if os.getenv("STAGE","local")=="local":
    with open('./env/local.yml') as file:
        for key, value in yaml.load(file).items():
            os.environ[key]=value if not value.startswith("${ssm:") else boto3.client('ssm').get_parameter(Name=value[6:-1])['Parameter']['Value']

def test_get():
    print(os.environ['SLACK_TOKEN'])
    print(os.environ['SLACK_ID'])
    print(os.environ['SLACK_ID_DEBUG'])
    print(os.environ['SLACK_ID_ERROR'])

if __name__ == '__main__':
    test_get()
