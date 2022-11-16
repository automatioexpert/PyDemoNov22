import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:/Users/valmiki/Desktop/Exe/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com")
driver.find_element(By.NAME,"q").send_keys("India Population 2022")
time.sleep(4)
driver.close()
print("Test Passed..Thank God for giving me this day!!")