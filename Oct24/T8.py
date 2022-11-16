import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://trust.salesforce.com/en/")

driver.find_element(By.CSS_SELECTOR, "button[title='Site Preferences']").click()
print('I am the best')
driver.quit()

