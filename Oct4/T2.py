import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://collegedunia.com/")
time.sleep(4)
print(driver.find_element(By.XPATH,"//h1").text)
driver.find_element(By.XPATH,"//button[contains(text(),'Search')]").click()

driver.find_element(By.XPATH,"//input[contains(@placeholder,'Search')]").send_keys("IIT DELHI")


