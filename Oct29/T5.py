import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://pypi.org/project/selenium/")
print(driver.find_element(By.CSS_SELECTOR,"div.notification-bar span.notification-bar__message").text)
