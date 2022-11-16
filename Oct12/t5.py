import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.cancer.gov/publications")
td=driver.find_elements(By.TAG_NAME,"a")
for t in td:
    print(t.text)
driver.close()