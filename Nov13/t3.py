from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.kwtglobal.com/")
print(driver.find_element(By.CSS_SELECTOR,"img[alt='KWT Global']").is_displayed())
print(driver.find_element(By.XPATH,"//h2").text)
driver.find_element(By.CSS_SELECTOR,"a[href*='culture']").click()
print("I am the best")