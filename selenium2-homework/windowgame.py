from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/windowgame.html")


mytable = driver.find_elements_by_xpath("//*[@id='button']/tbody/tr")
print(mytable)

for row in mytable.find_elements_by_css_selector('tr'):
    for cell in row.find_elements_by_tag_name('td'):
        print(cell.text)

all_rows = driver.find_element_by_xpath("//*[@id='button']/tbody/tr").click()