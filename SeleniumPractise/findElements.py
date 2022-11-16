import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
driver.find_element(By.ID,"login-input").send_keys("test@test.com")
elements=driver.find_elements(By.TAG_NAME,"a")
print("List size: ",len(elements))
for ele in elements:
    print(ele.get_attribute('href'))

print("I am the best..Thank God")
driver.close()


