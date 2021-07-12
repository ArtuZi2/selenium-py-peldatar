from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime, timezone, date
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/forms.html")

#nowutc = datetime.now(timezone.utc)
#print(nowutc)
time.sleep(2)

my_time = datetime(2021, 5, 6)
time_select = my_time.strftime("%Y.%m.%d")

driver.find_element_by_id("example-input-date").send_keys(time_select)

my_time1 = datetime(2012, 5, 5, 5, 5, 5, 555)
time_select1 = (my_time1.strftime("%Y-%m-%d %H:%M:%S:%f"))

driver.find_element_by_id("example-input-date-time").send_keys(time_select1)


my_time2 = datetime(2000, 12, 5, 12, 1)
time_select2 = (my_time2.strftime("00%Y-%m-%d %H:%M %p"))
driver.find_element_by_id("example-input-date-time-local").send_keys(time_select2)

my_time3 = datetime(1995, 12, 1)
time_select3 = (my_time3.strftime("%Y-%B"))

driver.find_element_by_id("example-input-month").send_keys(time_select3)

# driver.close()
