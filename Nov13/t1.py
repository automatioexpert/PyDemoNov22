from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://castore.com/collections/cricket-clothing")
print(driver.find_element(By.XPATH,"//div[contains(text(),'shipping')]").text)
print(driver.find_element(By.XPATH,"div.collection-top__title").text)
print(driver.find_element(By.XPATH,"div.rte.fade>span").text)
driver.find_element(By.CSS_SELECTOR,"a.search-trigger").click()
holder=driver.find_element(By.CSS_SELECTOR,"input[name='q']").get_attribute("placeholder")
print(holder)
driver.find_element(By.CSS_SELECTOR,"input[name='q']").send_keys("products",Keys.ENTER)
print("I am the world Champion..Thank God!!")

