"""import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/videos.html")
    html5video = driver.find_element_by_id("html5video")
    html5video.click()
    html5video.send_keys(Keys.SPACE)
    time.sleep(5)
    html5video.send_keys(Keys.SPACE)

    time.sleep(2)

    bunny = driver.find_element_by_xpath("/html/body/div/button[1]")
    bunny.click()
    time.sleep(3)
    bunny.click()

    youtube_video = driver.find_element_by_id("youtubeframe")
    youtube_video.click()
    youtube_video.send_keys(Keys.SPACE)
    time.sleep(5)
    youtube_video.click()

    """driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/videos.html")
    frame = driver.find_element_by_id("youtubeframe")
    driver.switch_to.frame(frame)
    time.sleep(2)
    driver.find_element_by_id("player").click()"""


finally:
    driver.close()"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()

options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/videos.html")

# video 01
try:
    html5video = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'html5video')))
    html5video.click()
    html5video.send_keys(Keys.SPACE)
    time.sleep(5)
    html5video.send_keys(Keys.SPACE)  # Stop video playing
except TimeoutException:
    print('A videó nem töltődött be, nem kattintható')

# video 02

start_stop_btn = driver.find_element_by_tag_name('button')
start_stop_btn.click()
time.sleep(5)
start_stop_btn.click()

# video 03
ifrm_ref = driver.find_element_by_id('youtubeframe')
driver.switch_to.frame(ifrm_ref)

player = driver.find_element_by_id('player')
player.click()
time.sleep(5)
player.click()

driver.switch_to.default_content()

driver.quit()