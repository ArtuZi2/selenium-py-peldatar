from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/another_form.html")


def fill_table(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element

send_button = driver.find_element_by_id("submit")

with open('table_in.csv', encoding='utf-8') as csvtable:
    csvreader = csv.reader(csvtable, delimiter=',')
    next(csvreader)

    for row in csvreader:
        print(row)
        fill_table("fullname").send_keys(row[0])
        fill_table("email").send_keys(row[1])
        fill_table("dob").send_keys(row[2])
        fill_table("phone").send_keys(row[3])
        send_button.click()
driver.find_element_by_tag_name("button").click()

driver.close()
