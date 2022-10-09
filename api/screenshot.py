from selenium import webdriver
from time import sleep
from werkzeug.utils import secure_filename
from utils import parse_url
from os import path
import logging

def init_screenshot():
    global driver, logger

    logger = logging.getLogger('urllib3.connectionpool')
    logger.setLevel(logging.INFO)
    logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
    logger.setLevel(logging.WARNING)

    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-extensions')
    options.add_argument("--disable-gpu");
    options.add_argument("--disable-crash-reporter");
    options.add_argument("--disable-in-process-stack-traces");
    options.add_argument("--disable-logging");
    options.add_argument("--disable-dev-shm-usage");
    options.add_argument("--log-level=3");
    options.add_argument("--output=/dev/null");
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)

def close_screenshot():
    driver.quit()

def screenshot(url: str)-> str:
    print(url, parse_url(url))
    url = parse_url(url)
    filename = secure_filename("{}.png".format(url))
    if path.exists("./tmp/{}".format(filename)):
        return filename
    #driver.implicitly_wait(1)
    driver.get(url)
    #driver.implicitly_wait(2)
    driver.execute_script('var x = document.createElement("style");x.innerHTML = "*{overflow:hidden !important}";document.querySelector("body").append(x)')
    driver.get_screenshot_as_file("./tmp/{}".format(filename))
    return filename