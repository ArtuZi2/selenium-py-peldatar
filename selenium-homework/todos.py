from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/todo.html")

todos = driver.find_elements_by_xpath('//checkbox')
print(todos)
print(type(todos))

for checkbox in todos:
    checkbox.click()
    vmi = driver.find_element_by_xpath(''/html/body/div/div/div/ul/li[1]/span)
    print(vmi.text)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/todo.html")
    todos = driver.find_elements_by_xpath('//*[@class="done-false"]')
    for todo in todos:
        print('TODO:', todo.text)
except NoSuchElementException as e:
    print('Element not found: ', e)
finally:
    driver.close()