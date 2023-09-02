import selenium
from selenium import webdriver
import streamlit as st

# Set the path to the ChromeDriver executable
chrome_driver_path = 'C:/ChromeDriver/chromedriver_win32/chromedriver'

# Configure Chrome to run in headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Enable headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration (may be necessary in some cases)

# Create a WebDriver instance with the Chrome options
driver = webdriver.Chrome( options=chrome_options)

driver.get('https://www.youtube.com/')

# Extract information from the web page
page_title = driver.title
page_source = driver.page_source
st.write('my result is : ')
st.write(page_title)
print(page_title)

# Close the WebDriver when done
driver.quit()
