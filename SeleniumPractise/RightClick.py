
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/valmiki/Desktop/Exe/chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
chains=ActionChains(driver)
drop=driver.find_element(By.XPATH,"//legend[contains(text(),'Dropdown Example')]")
#chains.context_click(drop).perform()
chains.double_click(drop).perform()
print("Right Click is done")
