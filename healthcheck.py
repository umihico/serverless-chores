import requests
import slack
import traceback

urls = [
    "https://umihi.co/",
    "https://portfoliohub.umihi.co/",
]


def healthcheck():
    results = {}
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            result = 'success'
        except Exception:
            result = 'failed'
            slack.error('Healthcheck Failed: ' + url +
                        "\n" + traceback.format_exc())
        results[url] = result
    return results


def test_healthcheck():
    assert all([v == "success" for v in healthcheck().values()])


if __name__ == '__main__':
    test_healthcheck()
