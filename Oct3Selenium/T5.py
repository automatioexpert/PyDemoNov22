import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.mindnode.com/")
driver.find_element(By.CSS_SELECTOR,"a[href*='learn']").click()
print(driver.find_element(By.XPATH,"//h1").text)
h3s=driver.find_elements(By.XPATH,"h3")
for h3 in h3s:
    print(h3.text)
driver.quit()
