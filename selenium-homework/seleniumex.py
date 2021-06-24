from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https:/python.org")
nemletezik = driver.find_element_by_id("nemletezik")
try:
    nemletezik = driver.find_element_by_id("nemletezik")
except NoSuchElementException:
    Print("Nincs ilyen elem")
