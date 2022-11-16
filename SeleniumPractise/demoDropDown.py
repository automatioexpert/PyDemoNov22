import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
dropDown=Select(driver.find_element(By.CSS_SELECTOR,"select#dropdown-class-example"))
dropDown.select_by_index(1)
dropDown.select_by_index(0)
dropDown.select_by_index(2)
dropDown.select_by_index(3)
print('Selected the value at 1 index')
