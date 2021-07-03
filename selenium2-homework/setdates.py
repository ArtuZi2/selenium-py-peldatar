from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

from datetime import datetime, timezone
import time
import _datetime

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/forms.html")

nowutc = datetime.now(timezone.utc)
print(nowutc)
time.sleep(2)
driver.find_element_by_id("example-input-month").send_keys(nowutc.strftime("%Y.%B"))

driver.find_element_by_id("example-input-date-time").send_keys(nowutc)