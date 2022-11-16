from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.salesforce.com/in/?ir=1")
driver.find_element(By.CSS_SELECTOR, "span+span.message").click()
print(driver.find_element(By.XPATH, "//header/h2").text)
driver.quit()
