import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://collegedunia.com/")
driver.find_element(By.CSS_SELECTOR,"a[href*='colleges']").click()
print(driver.find_element(By.XPATH,"//h1").text)
elements=driver.find_elements(By.XPATH,"//h3")
for ele in elements:
    print(ele.text)
driver.close()
print("I am the World Champion...Thank God!!")