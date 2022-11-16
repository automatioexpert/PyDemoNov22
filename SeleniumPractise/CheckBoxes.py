import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
cheks=driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
for check in cheks:
    check.click()

print("Check box status::")

cheks=driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
for check in cheks:
    print(check.is_enabled())

print("Selected all the checkoxes")

driver.close()