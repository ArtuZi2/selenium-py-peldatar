import pprint
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# import Action chains
from selenium.webdriver import ActionChains

extracted_data = []
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/pagination.html")


finally:
    pass
    driver.close()