import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
#driver.find_element(By.CSS_SELECTOR,"a[href*='basi']").click()
print(driver.find_element(By.XPATH,"//p[contains(text(),'Congra')]").text)
driver.close()
print("Test passed")