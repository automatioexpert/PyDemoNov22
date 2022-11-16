import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.mindnode.com/")
print(driver.find_element(By.XPATH,"//img[contains(@alt,'mind node')]").text)
print(driver.find_element(By.XPATH,"//h1").text)
elements=driver.find_elements(By.CSS_SELECTOR,"h2+p")
for ele in elements:
    print(ele.text)
driver.quit()
