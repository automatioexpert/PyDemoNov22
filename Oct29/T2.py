import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.oracle.com/")
driver.get("https://www.google.com")
driver.back()
print(driver.title)
driver.forward()
time.sleep(4)




