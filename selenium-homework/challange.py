from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

def challange():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://brave-desert-0a706e303.azurestaticapps.net/")


    message = "hellobello"
    user_message = driver.find_element_by_id("user_message").send_keys(message)
    driver.find_element_by_xpath('//*[@id="get-input"]/button').click()
    assert driver.find_element_by_xpath('//*[@id="display"]').text == message

    a = 1
    b = 2
    driver.find_element_by_id("sum1").send_keys(a)
    driver.find_element_by_id("sum2").send_keys(b)
    driver.find_element_by_xpath('//*[@id="gettotal"]/button')
    assert int(driver.find_element_by_id('displayvalue').text) == a + b