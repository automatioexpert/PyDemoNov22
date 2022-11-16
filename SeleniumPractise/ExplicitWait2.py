import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver =webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.yatra.com/")
origin=driver.find_element(By.CSS_SELECTOR,"input#BE_flight_origin_city")
#origin.click()

wait=WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input#BE_flight_origin_city"))).click()
print("Clicked after EC Wait!!")

origin.send_keys("New Delhi")
origin.send_keys(Keys.ENTER)
destination=driver.find_element(By.CSS_SELECTOR,"input#BE_flight_arrival_city")
destination.send_keys("New")

searchResults=driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
print(len(searchResults))

for result in searchResults:
    if "New York" in result.text:
        result.click()
        break

print("Test Passed.!!!")

