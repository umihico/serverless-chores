import boto3
import param
import requests
import io
import os

def post_message(slack_id, text):
    slack_id=slack_id if os.getenv('STAGE', 'local')=='prod' else param.get('SLACK_ID_DEBUG') # use muted debug channel when not prod
    slack_token = param.get('SLACK_TOKEN')
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_id,
        'text': text,
        # 'icon_url': slack_icon_url,
        'username': 'bot',
        # 'blocks': json.dumps(blocks) if blocks else None
    }).json()

def test_post_message():
    slack_id=param.get('SLACK_ID')
    text="this is post_message test."
    json=post_message(slack_id, text)
    print(json)
    assert json['ok'] is True
    return json

def log(*arg, **kw):
    '''
    print normaly on cloudwatch and send the same to my slack #log-debug
    '''
    slack_id=kw.get('slack_id', param.get('SLACK_ID_DEBUG'))
    if 'slack_id' in kw:
        del kw['slack_id']
    print(*arg, **kw)
    out=io.StringIO()
    kw['file']=out
    print(*arg, **kw)
    return post_message(slack_id, out.getvalue())

def test_log():
    assert log('this is log test')['ok'] is True

def error(*arg, **kw):
    kw['slack_id']=param.get('SLACK_ID_ERROR')
    return log(*arg, **kw)

def test_error():
    assert error('this is error test')['ok'] is True

if __name__ == '__main__':
    test_post_message()
    test_log()
    test_error()
    pass
