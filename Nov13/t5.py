from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.get("https://www.kwtglobal.com/services")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "a[href*='services']").click()
elements = driver.find_elements(By.CSS_SELECTOR, "div.image-subtitle.sqs-dynamic-text>p")
for e in elements:
    print(e.text)
