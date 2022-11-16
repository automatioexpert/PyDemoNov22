import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://pypi.org/project/selenium/")
print(driver.find_element(By.CSS_SELECTOR,"div.notification-bar").text)
driver.find_element(By.CSS_SELECTOR,"input#search").send_keys("products")

driver.find_element(By.CSS_SELECTOR,"i.fa.fa-search").click()
driver.find_element(By.CSS_SELECTOR,"i.fa.fa-copy").click()
print("I am the best expert on the Planet!!")
driver.quit()
