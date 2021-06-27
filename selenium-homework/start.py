from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://python.org")

driver.close()