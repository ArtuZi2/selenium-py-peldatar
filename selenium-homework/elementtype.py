from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:9999/trickyelements.html")
element1 = driver.find_element_by_id("element1")
element2 = driver.find_element_by_id("element2")
element2.click()
element3 = driver.find_element_by_id("element3")
element4 = driver.find_element_by_id("element4")
element5 = driver.find_element_by_id("element5")
element5.click()