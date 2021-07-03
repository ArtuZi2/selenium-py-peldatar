from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://react-card-2a6c5.web.app/")


add_to_cart = driver.find_elements_by_xpath('//div[@class="shelf-item"] and //div[@class="buy-btn"]')
print(len(add_to_cart))
for element in add_to_cart:
    print(element.text)
