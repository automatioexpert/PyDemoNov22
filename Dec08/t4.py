from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.nm.gov/")
elements=driver.find_elements(By.CSS_SELECTOR,"div.service-description")
print(len(elements))
for ele in elements:
    print(ele.text)
