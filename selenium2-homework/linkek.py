from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999")
links = driver.find_elements_by_xpath(("//a[@href]"))
print(links)
print(type(links))
print("Az összes link az oldalon:", len(links))

elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    print(elem.get_attribute("href"))
