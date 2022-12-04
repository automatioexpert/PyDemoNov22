from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import datetime
from selenium.webdriver.support.events import AbstractEventListener


logging.log()
logging.info("test1 executing")
baseURL = "https://letskodeit.teachable.com/"
driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.implicitly_wait(3)
driver.get(baseURL)

loginLink = driver.find_element(By.LINK_TEXT, "Login")
loginLink.click()

loginLink = driver.find_element(By.LINK_TEXT, "Login")
loginLink.click()

emailField = driver.find_element(By.ID, "user_email")
emailField.send_keys("test@email.com")

passwordField = driver.find_element(By.ID, "user_password")
passwordField.send_keys("abcabc")

loginButton = driver.find_element(By.NAME, "commit")
loginButton.click()

userIcon = driver.find_element(By.XPATH, ".//*[@id='navbar']//span[text()='User Settings']")
if userIcon is not None:
    print("Login Successful")
else:
    print("Login Failed")


