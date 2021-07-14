import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/simplevalidation.html")
    driver.find_element_by_id("test-email").send_keys("lary")

    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='e-w11uh9t9']"))).get_attrubite(
        "validationMessage")
    assert message is None
    assert message == "Please check your E-Mail format"

    driver.find_element_by_name("Password").click()
    message1 = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='e-w11uh9t9']"))).get_attrubite(
        "validationMessage")

    assert message1 is None
    assert message1 == "This field can't be empty"

    driver.find_element_by_id("e-ami9ay1w").click()



finally:
    pass
    #driver.close()