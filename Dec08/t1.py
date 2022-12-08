from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.nm.gov/")
status=driver.find_element(By.CSS_SELECTOR,"img[alt='Welcome to NewMexico.gov']").is_displayed()
print(status)
driver.find_element(By.XPATH,"//a[@href='/contact/']").click()
print(driver.find_element(By.CSS_SELECTOR,"h2.et_pb_module_header>span").text)
elements=driver.find_elements(By.CSS_SELECTOR,"div.agencies-contact-info>div")
for ele in elements:
    print(ele.text)
driver.quit()
print("Test Passed!!")