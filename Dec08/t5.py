from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.nm.gov/")
driver.find_element(By.XPATH,"//a[contains(text(),'Departments')]").click()
ele=driver.find_elements(By.CSS_SELECTOR,"div.agency-description>p")

for e in ele:
    print(e.text)
