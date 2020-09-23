from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import re
import time
from datetime import datetime

URL = 'https://mycutebaby.in/contest/participant/?n=5f54ac4d2e8a0'
desired_caps = webdriver.DesiredCapabilities.CHROME.copy()
desired_caps['acceptInsecureCerts'] = True
desired_caps['acceptSslCerts'] = True
i = 0
while True:
    driver = None;
    try:
        driver = webdriver.Chrome(desired_capabilities=desired_caps)
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight-100);")
        driver.find_element_by_xpath('//*[@id="v"]').send_keys('Bhai')
        driver.find_element_by_xpath('//*[@id="vote_btn"]').click()
        time.sleep(5)
        i = i + 1
        print('Voting no:', i, 'time:', datetime.now().strftime("%H:%M:%S"))
        driver.close()
        time.sleep(30*60)
    except:
        if driver is not None:
            driver.close()