import requests
import slack
import traceback

urls=[
    "https://umihi.co/",
    "https://portfoliohub.umihi.co/",
]

def healthcheck():
    results={}
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            result='success'
        except Exception as e:
            result='failed'
            slack.error('Healthcheck Failed: '+url+"\n"+traceback.format_exc())
        slack.log('healthcheck', result, url)
        results[url]=result
    return results

def test_healthcheck():
    return healthcheck()

if __name__ == '__main__':
    test_healthcheck()
