from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.salesforce.com/in/?ir=1")
driver.find_element(By.CSS_SELECTOR, "a[href*='terms-of-ser']").click()
elements=driver.find_elements(By.CSS_SELECTOR, "span.header-text")
for a in elements:
    print(a.text)

driver.quit()