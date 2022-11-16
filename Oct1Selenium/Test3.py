from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.selenium.dev/projects/")
print(driver.find_element(By.CSS_SELECTOR,"h2.card-title").text)
print(driver.find_element(By.CSS_SELECTOR,"h2.card-title+p").text)
driver.find_element(By.CSS_SELECTOR,"div.selenium-button-container>a[href*='sponsor']").click()
h1=driver.find_element(By.XPATH,"//h1").text
print(h1)

driver.find_element(By.CSS_SELECTOR,"a[href*='blog']").click()
print(driver.find_element(By.XPATH,"//h1[contains(text(),'Blog')]").text)
print(driver.find_element(By.CSS_SELECTOR,"div.pt-3.lead").text)

items=driver.find_elements(By.XPATH,"//h5")
for item in items:
    print(item.text)
print("Passed")

driver.close()