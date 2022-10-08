from selenium import webdriver
from time import sleep
from utils import generate_random_str
from werkzeug.utils import secure_filename
from utils import parse_url
from os import path

def init_screenshot():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)

def close_screenshot():
    driver.quit()

def screenshot(url: str)-> str:
    url = parse_url(url)
    filename = secure_filename("{}.png".format(url))
    if path.exists("./tmp/{}".format(filename)):
        return filename
    driver.get(url)
    #sleep(10)
    driver.execute_script('var x = document.createElement("style");x.innerHTML = "*{overflow:hidden !important}";document.querySelector("body").append(x)')
    #driver.get_screenshot_as_file("./tmp/screenshot_{}.png".format(generate_random_str(5)))
    driver.get_screenshot_as_file("./tmp/{}".format(filename))
    sleep(1)
    return filename