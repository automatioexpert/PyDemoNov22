import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:/Users/valmiki/Desktop/Exe/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com")
driver.find_element(By.NAME,"q").send_keys("India")
print("Test Passed..I am the best expert on the Planet..Thank God!!!")
time.sleep(4)
driver.quit()