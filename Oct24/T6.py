import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://trust.salesforce.com/en/")

elem = driver.find_elements(By.CSS_SELECTOR, "p>span")
for i in elem:
    print(i.text)
driver.quit()



