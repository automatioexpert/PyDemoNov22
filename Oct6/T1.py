from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:/Users/valmiki/Desktop/Exe/chromedriver.exe")
driver.maximize_window()
driver.get("https://reactjs.org/")
print(driver.find_element(By.XPATH,"//span[contains(text(),'preview')]").text)
driver.find_element(By.CSS_SELECTOR,"a[href*='tutorial']").click()
print(driver.find_element(By.XPATH,"//h1").text)
print("I am the world Champion of my Game..Thank God!!")