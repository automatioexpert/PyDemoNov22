from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.mos.com/join-us/")
print(driver.find_element(By.CSS_SELECTOR,"svg[alt='logo']").text)
driver.find_element(By.XPATH,"//a[contains(text(),'Learn')]").click()
print("I am the World Champion..!!!Thank God!!")
driver.quit()