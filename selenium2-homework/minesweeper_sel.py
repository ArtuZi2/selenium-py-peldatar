from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/minesweeper-game.html")