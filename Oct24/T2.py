from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://login.salesforce.com/?locale=in")
print(driver.title)
driver.find_element(By.CSS_SELECTOR, "a#forgot_password_link").click()
print(driver.find_element(By.CSS_SELECTOR, "h1#header").text)
print(driver.find_element(By.CSS_SELECTOR, "div.message").text)
driver.find_element(By.NAME, "cancel").click()
driver.find_element(By.CSS_SELECTOR, "a#video-link").click()
print("I am the top expert on the Planet!!Thank God!!")
driver.quit()