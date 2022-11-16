import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:/Users/valmiki/Desktop/Exe/chromedriver.exe")
driver.maximize_window()
driver.get("https://azimpremjiuniversity.edu.in/")
driver.find_element(By.CSS_SELECTOR,"a[href*='contact-us']").click()
time.sleep(3)
print(driver.find_element(By.CSS_SELECTOR,"a[href*='contact-us']").text)

paras=driver.find_elements(By.CSS_SELECTOR,"div>p")

for para in paras:
    print(para.text)

print("I am the World Champion ..Thank God!!!")

driver.quit()