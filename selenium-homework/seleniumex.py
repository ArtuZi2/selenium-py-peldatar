from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/todo.html")
l = driver.find_element_by_id("nemletezik")
driver.find_element_by_id()

try:
        driver.find_element_by_id("nemletezik")
except:
        print("Nincs ilyen elem")

finally:
        driver.close()
