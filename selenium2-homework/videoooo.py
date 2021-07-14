import time
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
    driver.close()