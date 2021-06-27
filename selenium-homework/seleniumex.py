from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https:/python.org")
driver.find_element_by_id("nemletezik")

def nemletezik():
    try:
        hiba = driver.find_element_by_id("nemletezik")

    except:
        print("Nincs ilyen elem")

    finally:
        driver.close()
