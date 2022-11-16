import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.armymwr.com/m/privacy-policy")
driver.find_element(By.CSS_SELECTOR,"img[src*='imc']").click()
print(driver.find_element(By.CSS_SELECTOR,"img[alt='mwr_logo.svg']").is_displayed())
print(driver.find_element(By.XPATH,"//h2[contains(text(),'MWR')]").text)
driver.find_element(By.CSS_SELECTOR,"div.close-button.float-right").click()
time.sleep(3)
print(driver.find_element(By.CSS_SELECTOR,"col-md-3.text-right>span").text)
driver.quit()
print("I am the Python Expert on the Planet!!")