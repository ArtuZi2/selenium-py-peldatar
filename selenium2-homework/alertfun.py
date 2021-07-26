"""import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# import Action chains
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/alert_playground.html")
    alert_button = driver.find_element_by_name("alert")
    alert_button.click()
    time.sleep(2)
    re_text = "I am alert"
    alert = driver.switch_to.alert
    assert(re_text == alert.text)
    print(alert.text)
    alert.accept()

    confirmation_button = driver.find_element_by_name("confirmation")
    confirmation_button.click()
    time.sleep(2)
    re_text2 = "I am confirm"
    alert = driver.switch_to.alert
    assert(re_text2 == alert.text)
    print(alert.text)
    alert.accept()

    def prompt(message):

        prompt_button = driver.find_element_by_name("prompt")
        prompt_button.click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.send_keys(message)
        alert.accept()
        time.sleep(1)
        demo = driver.find_element_by_xpath("//p[@id='demo']")
        assert demo.text == f"You entered: {message}"
        print(demo.text)

    prompt("Zita")

    double = driver.find_element_by_id("double-click")
    action = ActionChains(driver)
    action.double_click(double).perform()
    alert = driver.switch_to.alert
    re_text3 = "You double clicked me!!!, You got to be kidding me"
    assert (alert.text == re_text3)
    print(alert.text)
    time.sleep(1)
    alert.accept()

finally:
    driver.close()"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.headless = False
try:
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/alert_playground.html")


    def alert_action(prompt_text=''):
        alert = driver.switch_to.alert
        print(alert.text)
        if prompt_text.strip() != '':
            alert.send_keys(prompt_text)
        alert.accept()


    btns = driver.find_elements_by_tag_name('input')

    for btn in btns:
        prmpt = ''
        if btn.get_attribute('value') == 'Prompt':
            prmpt = 'Ezt figyeld!'

        if btn.get_attribute('value') != 'Double Click Me':
            btn.click()
            alert_action(prmpt)
        else:
            ac = ActionChains(driver)
            ac.double_click(btn).perform()
            alert_action()

    assert ('Ezt figyeld!' in driver.find_element_by_id('demo').text)
finally:
    driver.close()
    driver.quit()