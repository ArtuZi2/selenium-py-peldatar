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