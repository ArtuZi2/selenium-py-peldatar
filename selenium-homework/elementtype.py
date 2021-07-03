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




from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/trickyelements.html")
    found_elements = [driver.find_element_by_id("element1"), driver.find_element_by_id("element2"), driver.find_element_by_id("element3"),
                      driver.find_element_by_id("element4"), driver.find_element_by_id("element5")]
    for element in found_elements:
        if element.tag_name == "button" or element.get_attribute("onclick") is not None:
            button_text = element.text
            element.click()
            break
    message_text = driver.find_element_by_id("result").text
    assert f'{button_text} was clicked' == message_text
    print("test finished OK")

except NoSuchElementException as e:
    print('Element not found: ', e)
finally:
    driver.close()