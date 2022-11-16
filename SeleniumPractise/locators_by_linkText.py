import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class DemoFindElementByName():
    def locate_by_name(self):
        driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        driver.find_element(By.PARTIAL_LINK_TEXT,"My Accou").click()
        time.sleep(4)

findByID=DemoFindElementByName()
findByID.locate_by_name()

