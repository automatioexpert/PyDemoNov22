import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://collegedunia.com/")
driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
time.sleep(5)
items=driver.find_elements(By.CSS_SELECTOR,"ul>li")
for it in items:
    print(it.text)
driver.quit()
print("I am the best in the World!!")