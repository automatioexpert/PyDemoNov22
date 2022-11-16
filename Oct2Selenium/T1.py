from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:/Users/valmiki/Desktop/Exe/chromedriver.exe")
driver.maximize_window()
driver.get("https://azimpremjiuniversity.edu.in/field-studies-in-education")

topics=driver.find_elements(By.CSS_SELECTOR,"div>h3")

for topic in topics:
    print(topic.text)

print("I am the best expert on the Planet...!!")