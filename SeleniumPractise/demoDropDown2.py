import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://developer.salesforce.com/signup")
dropDown=Select(driver.find_element(By.CSS_SELECTOR,"select[name$='job_role']"))
dropDown.select_by_index(1)
dropDown.select_by_index(2)
print("I am the Top Expert on the Planet")
