import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
continueBtn=driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
continueBtn.screenshot(".\\test_vv_24Sep2022_11.30PM_IST.png")
continueBtn.click()
time.sleep(2)
driver.get_screenshot_as_file(".\\test_file.jpg")
print("Done..!!")
