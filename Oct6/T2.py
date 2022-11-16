from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:/Users/valmiki/Desktop/Exe/chromedriver.exe")
driver.maximize_window()
driver.get("https://reactjs.org/")
print(driver.current_window_handle)
print(driver.title)
driver.quit()
driver.close()