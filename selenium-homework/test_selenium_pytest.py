import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# Step 1, add import for options
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os


class TestDefaultSuite():
    def setup_method(self, method):
        runenv = os.environ['RUNENV']
        if runenv == "GITHUB":
            chrome_options = Options()  # Step 2, create options object
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--headless")
            # Step 3, pass chrome_options object to Chrome() constructor
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        else:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_firstTest(self):
        self.driver.get("https://www.google.com/")
        self.driver.set_window_size(980, 698)
        self.driver.find_element(By.NAME, "q").click()
        self.driver.find_element(By.NAME, "q").send_keys("köpönyeg")
        self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
        elements = self.driver.find_elements(By.XPATH, "//span[contains(.,\'Köpönyeg\')]")
        assert len(elements) > 0