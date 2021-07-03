from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/todo.html")
l = driver.find_element_by_id("nemletezik")
driver.find_element_by_id()

try:
        driver.get("http://localhost:9999/todo.html")
        l = driver.find_element_by_id("nemletezik")
except NoSuchElementException as e:
        print("Nincs ilyen elem"), e

finally:
        driver.close()
