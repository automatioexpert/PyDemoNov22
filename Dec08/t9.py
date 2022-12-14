from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.nm.gov/online-services/")
driver.find_element(By.CSS_SELECTOR, "a[href*='news']").click()
title=driver.find_elements(By.CSS_SELECTOR, "div.news-title")
for t in title:
    print(t.text)

driver.quit()