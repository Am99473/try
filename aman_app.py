import os
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = str(os.environ.get("GOOGLE_CHROME_BIN"))
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"))
driver.get("http://www.python.org")
print(driver.title)