import requests
import slack
import traceback
import pymysql
import os
import env


def healthcheck():
    return {
        **healthcheck_web(),
        **healthcheck_db(),
    }


def healthcheck_db():
    envs = {
        "db_stg": {
            "host": os.getenv('MYSQL_HOST_STG'),
            "user": os.getenv('MYSQL_USER_STG'),
            "passwd": os.getenv('MYSQL_ROOT_PASSWORD_STG'),
            "port": int(os.getenv("MYSQL_PORT_STG")),
        },
        "db_prod": {
            "host": os.getenv('MYSQL_HOST_PROD'),
            "user": os.getenv('MYSQL_USER_PROD'),
            "passwd": os.getenv('MYSQL_ROOT_PASSWORD_PROD'),
            "port": int(os.getenv("MYSQL_PORT_PROD")),
        },
    }
    result = {}
    for env_name, kw in envs.items():
        try:
            pymysql.connect(**kw, connect_timeout=5)
            result[env_name] = 'success'
        except Exception:
            slack.error('DB Healthcheck Failed: ' + env_name.upper() +
                        "\n" + traceback.format_exc())
            result[env_name] = 'failed'
    return result


def healthcheck_web():
    urls = [
        "https://umihi.co/",
        "https://portfoliohub.umihi.co/",
    ]
    results = {}
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            result = 'success'
        except Exception:
            result = 'failed'
            slack.error('WEB Healthcheck Failed: ' + url.upper() +
                        "\n" + traceback.format_exc())
        results[url] = result
    return results


def test_healthcheck():
    assert all([v == "success" for v in healthcheck().values()])


if __name__ == '__main__':
    test_healthcheck()
