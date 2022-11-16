import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/valmiki/Desktop/Exe/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.snapdeal.com/products/mens-footwear-sports-shoes?sort=plrty")
left=driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]").click()
right=driver.find_element(By.XPATH,"//a[contains(@class,'right-handle')]").click()
ActionChains(driver).click_and_hold(left).pause(1).move_by_offset(50,0).release().perform()
time.sleep(2)
print("Silded to Right direction")
