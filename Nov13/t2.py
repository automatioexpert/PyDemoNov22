from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.pluralsight.com/")
if(driver.find_element(By.CSS_SELECTOR,"button.cookie-notification-button.allow").is_displayed()):
    driver.find_element(By.CSS_SELECTOR,"button.cookie-notification-button.allow").click()
driver.find_element(By.CSS_SELECTOR,"a[href*='get-started']").click()
driver.find_element(By.CSS_SELECTOR,"button[aria-label='Sign in']").click()



