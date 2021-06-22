from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https:/python.org")
nemletezik = driver.find_element_by_id("nemletezik")

driver.close()