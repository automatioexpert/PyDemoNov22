import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/")
driver.find_element(By.CSS_SELECTOR,"a[href*='elements']").click()
print(driver.find_element(By.XPATH,"//h3").text)
element=driver.find_element(By.XPATH,"//button[contains(text(),'Add')]")
print(element.text)
time.sleep(3)
print(driver.find_element(By.XPATH,"//button[contains(text(),'Delete')]").text)
#driver.find_element(By.CSS_SELECTOR,"button[onclick='deleteElement()']").click()
print("Test Passed!!!")
driver.close()