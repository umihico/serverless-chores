from selenium import webdriver
import os
import itertools
import time
import env


def get_options():
    options = webdriver.ChromeOptions()
    options.binary_location = "/opt/python/bin/headless-chromium"
    options.add_argument("--headless")
    options.add_argument("--homedir=/tmp")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-infobars")
    options.add_argument("--no-sandbox")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--enable-logging")
    options.add_argument("--log-level=0")
    options.add_argument("--single-process")
    options.add_argument("--ignore-certificate-errors")
    return options


class ServerlessChrome(webdriver.Chrome):
    def __init__(self):
        kw = {'executable_path': "/opt/python/bin/chromedriver", 'options': get_options(
        )} if os.environ['STAGE'] != "local" else {}
        super().__init__(**kw)


def test_chrome():
    chrome = ServerlessChrome()
    try:
        chrome.get("https://www.google.com/")
        chrome.find_element_by_xpath("//input")
        title = chrome.title
        assert title == "Google"
    except Exception:
        raise
    finally:
        chrome.quit()


if __name__ == '__main__':
    test_chrome()
