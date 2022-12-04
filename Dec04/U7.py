from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.get("https://nodejs.org/en/")
logo = driver.find_element(By.CSS_SELECTOR, "a#logo")
logo.send_keys("......................")
status = logo.is_displayed()
print(status)

userIcon = driver.find_element(By.XPATH, ".//*[@id='navbar']//span[text()='User Settings']")
if userIcon is not None:
    print("Login Successful")
else:
    print("Login Failed")


driver.quit()
