import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.oracle.com/")

diff = driver.find_element(By.XPATH, "//div[contains(text(),'different')]")

action = ActionChains(driver)
action.move_to_element(diff).perform()

print("I am the top expert on the Planet!!!")

time.sleep(6)

driver.quit()






