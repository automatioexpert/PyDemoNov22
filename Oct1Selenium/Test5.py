import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/")
parentWindow=driver.current_window_handle
driver.find_element(By.CSS_SELECTOR,"a[href*='abtest']").click()
print(driver.find_element(By.CSS_SELECTOR,"div.example>h3").text)
print(driver.find_element(By.CSS_SELECTOR,"div.example>h3+p").text)
print(driver.find_element(By.CSS_SELECTOR,"div.large-4.large-centered.columns").text)
driver.find_element(By.CSS_SELECTOR,"a[href*='elemen']").click()
handles=driver.window_handles
time.sleep(6)

for handle in handles:
    if(handle!=parentWindow):
        driver.switch_to(handle)

print(driver.find_element(By.CSS_SELECTOR,"h2.subheader").text)
print("I am the best")
