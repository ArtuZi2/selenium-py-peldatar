from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/")

def navigate_to_general():
    link = driver.find_element_by_xpath('//a[text()="General text and other elements"]')
    link.click()

try:
    navigate_to_general()
    driver.back()

    anchors = driver.find_elements_by_xpath('//header/small//a')

    for a in anchors:
        time.sleep(1.0)
        a.click()
finally:
    driver.close()