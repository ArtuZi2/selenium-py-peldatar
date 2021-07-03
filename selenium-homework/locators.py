from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/kitchensink.html")


def loco():
    my_name = Zita
    driver.find_element_by_xpath('//*[@id="name"]').click()
    driver.find_element_by_id("name").send_keys(my_name)

    driver.find_element_by_id("hide-textbox").click()
    driver.find_element_by_id("show.textbox").click()

    driver.find_element_by_xpath('button[@id="mousehover"]').click()

    driver.close()

try:
    driver.get("http://localhost:9999/kitchensink.html")

    driver.find_element_by_name("cars")
    driver.find_element_by_id("bmwradio")
    driver.find_element_by_xpath('//*[@id="openwindow"]')

    print("test finished OK")

except NoSuchElementException as e:
    print('Element not found: ', e)
finally:
    driver.close()
