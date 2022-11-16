import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.cancer.gov/publications")
le=driver.find_element(By.CSS_SELECTOR,"a[href*='grants']")
#le.click()
driver.find_element(By.CSS_SELECTOR,"ul>li>a[href*='syndication']").click()
print('I am the best')
