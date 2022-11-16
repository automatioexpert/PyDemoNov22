from selenium import webdriver;
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://acumenacademy.org/learn/")
driver.find_element(By.CSS_SELECTOR ,"a[href*='terms']").click()
terms=driver.find_element(By.CSS_SELECTOR,"h2#terms-of-use").text;
print(terms)
print(driver.find_element(By.CSS_SELECTOR,"h2#terms-of-use+p").text)
print(driver.find_element(By.CSS_SELECTOR,"h3#i-agreement-to-terms").text)
driver.find_element(By.CSS_SELECTOR,"h4+a+a[href*='contact']").click()
print(driver.find_element(By.XPATH,"//h2").text)
print(driver.find_element(By.CSS_SELECTOR,"h2+p").text)
print("I am the top expert on the Planet..Thank You God for trillion times")
driver.quit()