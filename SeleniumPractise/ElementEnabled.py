import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.yatra.com/")
status=driver.find_element(By.XPATH,"//span[contains(text(),'Buses')]").is_enabled()
print("Status of the Element is : ",status)
more=driver.find_element(By.CSS_SELECTOR,".more-arr").is_enabled()
print(more)
driver.close()



