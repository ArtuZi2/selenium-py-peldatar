from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://techstepacademy.com/trial-of-the-stones")

text1 = "rock"
text2 = "bamboo"
text3 = "Jessica"
driver.find_element_by_name("r1Input").send_keys(text1)
driver.find_element_by_id("r1Btn").click()
driver.find_element_by_id("r2Input").send_keys(text2)
driver.find_element_by_id("r2Btn").click()


price = driver.find_element_by_xpath("//*[@id=block-05ea3afedc551e378bdc]/div/div[3]/p")
price2 = driver.find_element_by_xpath("//*[@id=block-05ea3afedc551e378bdc]/div/div[4]/p")
if price > price2:
    print(price)
else:
    print(price2)

driver.find_element_by_id("r3Input").send_keys(text3)
driver.find_element_by_id("r3Btn").click()

driver.find_element_by_id("checkButn").click()
