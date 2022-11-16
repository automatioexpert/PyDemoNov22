import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.almarai.com/")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Looking for?']").send_keys("food")
driver.find_element(By.CSS_SELECTOR,"input+img[src*='search']").click()
