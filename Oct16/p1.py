from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window();
driver.get("https://www.ltts.com/")
driver.find_element(By.CSS_SELECTOR,"div li a[href*='industry/telecommunications']").click()
print('I am the top expert on the Planet!!')