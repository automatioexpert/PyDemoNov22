from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
url = "https://www.codementor.io/selenium-experts"
driver.get(url)
print(driver.find_element(By.CSS_SELECTOR,"a[title='Codementor homepage']").is_displayed())
print(driver.find_element(By.XPATH,"//h1[contains(text(),'developer')]").text)
driver.find_element(By.XPATH,"//span[contains(text(),'HELP')]").click()
print(driver.find_element(By.XPATH,"//img[contains(@alt,'codementor')]").text)
print(driver.find_element(By.XPATH,"//img[contains(@alt,'codementor')]/following-sibling::p").text)
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Stewart Vishwa Baliyari")