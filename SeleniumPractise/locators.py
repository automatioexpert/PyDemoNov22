import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.yatra.com/")
headingGod=driver.find_element(By.CSS_SELECTOR,"span.main-heading").text
print(headingGod)
time.sleep(1)

dep=driver.find_elements(By.CSS_SELECTOR,"div.time")
for de in dep:
    print(de.text)

print("Thank You God!!!")