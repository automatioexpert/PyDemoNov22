import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/valmiki/Desktop/Exe/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
source=driver.find_element(By.CSS_SELECTOR,"div#draggable")
destination=driver.find_element(By.CSS_SELECTOR,"div#droppable")

#ActionChains(driver).drag_and_drop(source,destination).perform()
time.sleep(4)

ActionChains(driver).drag_and_drop_by_offset(source,50,89).perform()
time.sleep(2)

print("Drag and Drop is success..Thank God!!")
driver.quit()