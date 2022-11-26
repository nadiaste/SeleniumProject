from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

HOST = "https://demoqa.com/text-box"

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
print('maximizing the browser window')
driver.maximize_window()

print("Starting the test with various locator to use in find_element() method")
driver.get(HOST)
time.sleep(5)

fullname = driver.find_element(By.ID, 'userName')
fullname.send_keys('John')
# driver.find_element(By.NAME, "q")
driver.find_element(By.TAG_NAME, 'textarea').send_keys("selenium found 'textarea on html, this is the first element of")
element_list = driver.find_elements(By.CLASS_NAME, 'form-control') #list
print(element_list)
print(f"Number of elements in primary_buttons list: {len(element_list)}")
time.sleep(5)

print('opening the google for link text locator..')
driver.get()
# primary_buttons = driver.find_elements(By.CLASS_NAME, 'btn btn-')
# email_input = driver.find_element(By.CLASS_NAME, 'mr-sm-2 form-control').send_keys("My@email.com")
#
# driver.find_element(By.ID, 'search')
# driver.find_element(By.NAME, 'q')


driver.find_element(By.XPATH, '//form[0]/div[0]/input[0]')
driver.find_element(By.CSS_SELECTOR, '#search')
driver.find_element(By.LINK_TEXT, 'Log In')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Log')