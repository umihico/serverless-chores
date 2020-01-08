from selenium import webdriver
import os
import itertools
import time
import env

def Options():
    options = webdriver.ChromeOptions()
    if os.environ['STAGE']!="local":
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

def Chrome():
    chrome = webdriver.Chrome(os.getenv("CHROME_EXECUTABLE_PATH"), options=Options())
    return chrome

webdriver.Chrome.xpaths=webdriver.Chrome.find_elements_by_xpath
webdriver.Chrome.xpath=webdriver.Chrome.find_element_by_xpath

def wait_element(self, xpath, timeout=None):
    start_time=time.time()
    for _ in itertools.count():
        if len(self.xpaths(xpath)):
            break
        if timeout and time.time()>start_time+timeout:
            raise Exception(' '.join(["timeoutException. xpath:", xpath,  "is not found"]))
        time.sleep(0.1)

webdriver.Chrome.wait_element=wait_element

def test_chrome():
    chrome=Chrome()
    try:
        chrome.get("https://www.google.com/")
        assert len(chrome.xpaths("//input"))>0
        title = chrome.title
        assert title=="Google"
        chrome.wait_element("//img")
    except Exception as e:
        raise
    finally:
        chrome.quit()

if __name__ == '__main__':
    test_chrome()
