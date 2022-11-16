from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = "C:\\Users\\valmiki\Desktop\Exe\\chromedriver.exe")
driver.get("https://state.bihar.gov.in/main/CitizenHome.html")
driver.find_element(By.CSS_SELECTOR, "a[title='Menu']").click()
driver.find_element(By.XPATH, "//a[contains(text(),'Bihar State Profile')]").click()
print(driver.find_element(By.CSS_SELECTOR, "ol.breadcrumb").text)
print(driver.find_element(By.CSS_SELECTOR, "p[align*='justify']").text)

print("I am the best expert on the Planet..Thank God")
driver.close()
