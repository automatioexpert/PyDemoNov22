from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.nm.gov/online-services/")
print(driver.find_element(By.CSS_SELECTOR,"div.et_pb_module_inner").text)
driver.quit()