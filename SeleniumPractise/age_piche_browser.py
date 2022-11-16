from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.yatra.com/")
driver.find_element(By.XPATH,"//span[contains(text(),'Hotels')]").click()
driver.back()
print("Navigate back")
driver.forward()
print("Navigated forward in the browser")
