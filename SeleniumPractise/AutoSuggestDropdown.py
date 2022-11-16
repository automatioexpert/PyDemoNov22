import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver =webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.yatra.com/")
origin=driver.find_element(By.CSS_SELECTOR,"input#BE_flight_origin_city")
origin.click()
time.sleep(2)
origin.send_keys("New Delhi")
time.sleep(2)
origin.send_keys(Keys.ENTER)
time.sleep(2)
destination=driver.find_element(By.CSS_SELECTOR,"input#BE_flight_arrival_city")
destination.send_keys("New")
time.sleep(2)
searchResults=driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
print(len(searchResults))

for result in searchResults:
    if "New York(NYC)" in result.text:
        result.click()
        break

print("Test Passed.!!!")

