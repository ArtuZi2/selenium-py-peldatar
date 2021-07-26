"""import pprint
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import csv

try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    extracted_data = []
    driver.get("http://localhost:9999/pagination.html")
    while True:
        time.sleep(2)
        table = driver.find_element_by_xpath("//table[@id='contacts-table']/tbody")
        rows = table.find_elements_by_tag_name("tr")
        for row in rows:
            data_row = {}
            cells = row.find_elements_by_tag_name("td")
            data_row["id"] = cells[0].text
            data_row["first_name"] = cells[1].text
            data_row["second_name"] = cells[2].text
            data_row["surname"] = cells[3].text
            data_row["second_surname"] = cells[4].text
            data_row["birth_date"] = cells[5].text
            if cells[1].text.startswith('A'):
                extracted_data.append(data_row)
        next_button = driver.find_element_by_id("next")
        if not next_button.is_enabled():
            break
        else:
            next_button.click()
        pprint.pprint(extracted_data)
        print(len(extracted_data))

    with open('start_a.csv', 'w', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(extracted_data)

finally:
    driver.close()"""

import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.headless = False
try:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/pagination.html")

    collected_data = []

    head = [th.text for th in driver.find_elements_by_xpath('//table[@id="contacts-table"]/thead/tr/th')]

    while True:
        for tr in driver.find_elements_by_xpath('//table[@id="contacts-table"]/tbody/tr'):
            td_texts_list = [td.text for td in tr.find_elements_by_tag_name('td')]
            row = dict(zip(head, td_texts_list))
            if row['First name'].startswith('A'):
                collected_data.append(row)

        next_btn = driver.find_element_by_id('next')

        if next_btn.is_enabled():
            next_btn.click()
        else:
            break

    with open('start_with_A.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=head)
        writer.writeheader()
        for data_row in collected_data:
            writer.writerow(data_row)
finally:
    driver.close()
    driver.quit()
