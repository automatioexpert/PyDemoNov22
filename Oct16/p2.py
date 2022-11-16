from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window();
driver.get("https://mcube.vmctechnologies.com/")

print(driver.find_element(By.CSS_SELECTOR,"img[alt='Key icon']").text)
print(driver.find_element(By.NAME,"login_username").get_attribute("placeholder"))
driver.find_element(By.NAME,"login_username").send_keys("Dinga3493348")

print(driver.find_element(By.NAME,"login_password").get_attribute("placeholder"))
driver.find_element(By.NAME,"login_password").send_keys("Pinga347347374");

driver.find_element(By.ID,"validator").send_keys("YRMBDCQ")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

print(driver.find_element(By.CSS_SELECTOR,"div.alert.error ").text)
driver.find_element(By.CSS_SELECTOR,"button.close").click()

driver.find_element(By.XPATH,"//b[contains(text(),'Classic View')]").click()
error=driver.find_element(By.CSS_SELECTOR,"div.cnt223").text
print(error)

driver.quit()
print('I am the top expert on the Planet!!')