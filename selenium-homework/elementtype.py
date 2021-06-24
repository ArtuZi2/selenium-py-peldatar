#nameerror-t még nem oldottam meg, küzdök vele

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:9999/trickyelements.html")

element1 = driver.find_element_by_id("element1")
if driver.find_element_by_id("element1").get_attribute("type"):
    element1.click()

element2 = driver.find_element_by_id("element2")
if driver.find_element_by_id("element2").get_attribute("type"):
    element2.click()

element3 = driver.find_element_by_id("element3")
if driver.find_element_by_id("element3").get_attribute("type"):
    element3.click()

element4 = driver.find_element_by_id("element4")
if driver.find_element_by_id("element4").get_attribute("type"):
    element4.click()

element5 = driver.find_element_by_id("element5")
if driver.find_element_by_id("element5").get_attribute("type"):
    element5.click()

label = driver.find_element_by_id("result")
print(label.text)

assert(label.text == f"{button.text} was clicked")