from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/editable-table.html")

add_button = driver.find_element_by_tag_name("button").click()


"""def find_and_clear_by_name(name):
    element = driver.find_element_by_name(name)
    return element

add_button = driver.find_element_by_tag_name("button").click()

with open("adatok.csv", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        print(row)
        find_and_clear_by_name("name").send_keys(row[0])
        find_and_clear_by_name("price").send_keys(row[1])
        find_and_clear_by_name("qty").send_keys(row[2])
        find_and_clear_by_name("category").send_keys(row[3])
        add_button"""