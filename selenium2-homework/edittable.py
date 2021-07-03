from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/editable-table.html")

def find_and_clear_by_id(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element

add_button = driver.find_element_by_id("add")

with open("data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        print(row)
        find_and_clear_by_id("product").send_keys(row[0])
        find_and_clear_by_id("quantity").send_keys(row[1])
        find_and_clear_by_id("price").send_keys(row[2])
        add_button.click()