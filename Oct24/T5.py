import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.salesforce.com/in/?ir=1")
print(driver.find_element(By.CSS_SELECTOR, "a[href*='tel']").text)
driver.find_element(By.CSS_SELECTOR, "li.page-footer_links_item a[href*='trust']")
time.sleep(3000)
driver.quit()

