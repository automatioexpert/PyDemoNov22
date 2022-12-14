from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.nm.gov/")
driver.find_element(By.CSS_SELECTOR,"a.main-menu-link").click()
print(driver.find_element(By.CSS_SELECTOR,"h4.et_pb_module_header>span").text)
links=driver.find_elements(By.CSS_SELECTOR,"h4.et_pb_module_header>a")
for link in links:
    print(link.text)
print("Test is completed!!!")
