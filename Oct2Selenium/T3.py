import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:/Users/valmiki/Desktop/Exe/chromedriver.exe")
driver.maximize_window()
driver.get("https://azimpremjiuniversity.edu.in/study-undergraduate")
driver.find_element(By.XPATH,"//span[contains(text(),'Research')]").click()
driver.find_element(By.CSS_SELECTOR,"a[href*='funding']").click()
time.sleep(3)
print(driver.find_element(By.XPATH,"//header/h1").text)

elements =driver.find_elements(By.CSS_SELECTOR,"tbody>tr>td")

for ele in elements:
    print(ele.text)


