from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html")

tags=driver.find_elements(By.TAG_NAME,"a")

for x in tags:
    print(x.get_attribute("href"))




