from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()

driver.implicitly_wait(0.5)
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")

# identify dropdown with Select class
sel = Select(driver.find_element(By.XPATH,"//select[@name='continents']"))
#select by select_by_visible_text() method
sel.select_by_visible_text("Europe")
time.sleep(0.8)
#select by select_by_index() method
sel.select_by_index(0)
driver.close()