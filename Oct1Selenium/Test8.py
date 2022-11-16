import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("http://localhost:8080/")
print(driver.find_element(By.CSS_SELECTOR,"div#main-message").text)
driver.close()
