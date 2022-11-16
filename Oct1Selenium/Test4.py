from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/")
print(driver.find_element(By.CSS_SELECTOR,"h1.heading").text)
print(driver.find_element(By.CSS_SELECTOR,"h1.heading+h2").text)
topics=driver.find_elements(By.CSS_SELECTOR,"ul>li")
for topic in topics:
    print(topic.text)



