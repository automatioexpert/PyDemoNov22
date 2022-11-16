import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.yatra.com/")
print(driver.find_element(By.CSS_SELECTOR,"a#booking_engine_buses").get_attribute("href"))
print(driver.find_element(By.CSS_SELECTOR,"a#booking_engine_buses").get_attribute("target"))
print(driver.find_element(By.CSS_SELECTOR,"a#booking_engine_buses").get_attribute("title"))
print(driver.find_element(By.CSS_SELECTOR,"a#booking_engine_buses").get_attribute("class"))
print(driver.find_element(By.CSS_SELECTOR,"a>i.ico-newHeaderLogo").get_attribute("class"))


print("I am the World Champion..Thank God!!")
driver.quit()



