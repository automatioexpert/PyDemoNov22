import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.mindnode.com/")
driver.find_element(By.CSS_SELECTOR,"a[href*='support']").click()
time.sleep(3)
print(driver.find_element(By.XPATH,"//h1").text)
print(driver.find_element(By.CSS_SELECTOR,"div.support__header").text)

lbs=driver.find_elements(By.CSS_SELECTOR,"a.supportSearch__question--label")
for lb in lbs:
    print(lb.text)

print('I am the World Champion of my field')
driver.quit()