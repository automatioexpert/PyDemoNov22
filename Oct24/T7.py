import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://trust.salesforce.com/en/")
driver.find_element(By.CSS_SELECTOR, "p#site-url").click()

le = driver.find_elements(By.CSS_SELECTOR, "span.slds-truncate")

for l in le:
    print(l.text)

driver.quit()
