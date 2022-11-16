
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/valmiki/Desktop/Exe/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")
driver.switch_to.frame("iframeResult")
print(driver.find_element(By.XPATH,"//h1[contains(text(),'iframe')]").text)
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"#tryhome").is_displayed())
driver.quit()
print("I am the Top Expert on the Planet..Thank God!!!")