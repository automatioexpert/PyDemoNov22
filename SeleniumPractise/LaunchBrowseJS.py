import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/valmiki/Desktop/Exe/chromedriver.exe")
driver.maximize_window()
#driver.get("https://www.google.com")
driver.execute_script("window.open('https://www.google.com','_self')")
print("Chrome Launched..!!!")
time.sleep(3)
driver.close()