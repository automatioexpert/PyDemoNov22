from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.kwtglobal.com/culture")
driver.find_element(By.CSS_SELECTOR,"a[href*='expertise']").click()
print(driver.find_element(By.XPATH,"//h2[contains(text(),'Our Expert')]").text)
elements=driver.find_elements(By.XPATH,"//h3")
for element in elements:
    print(element.text)
print("===================")
elements=driver.find_elements(By.CSS_SELECTOR,"h3+p")
for ele in elements:
    print(ele.text)
print("Test Passed")