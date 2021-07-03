from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time

opt = Options()

opt.headless = True
driver = webdriver.Chrome()

driver.get('http://www.rpachallenge.com/?lang=EN')

with open('challenge.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        first_name = driver.find_element_by_xpath('//input[@ng-reflect="labelFirstName"]')
        first_name.clear()
        first_name.send_keys(elem)
        last_name = driver.find_element_by_xpath('//input[@ng-reflect="labelLastName"]')
        last_name.clear()
        last_name.send_keys(elem)
        company_name = driver.find_element_by_xpath('//input[@ng-reflect="labelCompanyName"]')
        role_in_company = driver.find_element_by_xpath('//input[@ng-reflect="labelRole"]')
        address = driver.find_element_by_xpath('//input[@ng-reflect="labelAddress"]')
        email = driver.find_element_by_xpath('//input[@ng-reflect="labelEmail"]')
        phone_number = driver.find_element_by_xpath('//input[@ng-reflect="labelPhone"]')


driver.close()