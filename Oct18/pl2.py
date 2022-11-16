import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = "C:\\Users\\valmiki\Desktop\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://state.bihar.gov.in/main/CitizenHome.html")
driver.find_element(By.CSS_SELECTOR,"i[title='Select Orange Theme']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"i[title*='Select Green Theme']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"i[title*='Select Blue Theme']").click()
time.sleep(5)
print("I am the best expert on the planet..Thank God!!")
driver.quit()