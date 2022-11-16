from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:/Users/valmiki/Desktop/Exe/chromedriver.exe")
driver.maximize_window()
driver.get("https://azimpremjiuniversity.edu.in/field-studies-in-education")
driver.find_element(By.XPATH,"//span[contains(text(),'Study')]").click()
driver.find_element(By.CSS_SELECTOR,"a[href*='-undergraduate']").click()
ele=driver.find_elements(By.XPATH,"//h4")

for e in ele:
    print(e.text)

print("I am the World Champion")
driver.quit()
