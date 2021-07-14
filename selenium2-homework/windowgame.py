from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/windowgame.html")

    button_list = driver.find_elements_by_tag_name("button")
    for _ in range(10):
        button_list[random.randint(0, len(button_list)-1)].click()
        driver.switch_to.window(driver.window_handles[-1])
        print(driver.find_element_by_tag_name("h1").text)
        driver.switch_to.window(driver.window_handles[0])
finally:
    pass
    #driver.close()


"""mytable = driver.find_elements_by_xpath("//*[@id='button']/tbody/tr")
print(mytable)

for row in mytable.find_elements_by_css_selector('tr'):
    for cell in row.find_elements_by_tag_name('td'):
        print(cell.text)

all_rows = driver.find_element_by_xpath("//*[@id='button']/tbody/tr").click()"""