from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.timeouts.implicit_wait(10)
driver.get("https://www.nm.gov/")
strive=driver.find_element(By.XPATH,"//span[contains(text(),'strive')]").text
print(strive)
ele=driver.find_elements(By.CSS_SELECTOR,"h2.et_pb_module_header")
try:
    print(ele.text)
except:
    print("Attribute error exception has been found!!")
driver.find_element(By.CSS_SELECTOR,"a[href*='search']").click()
print(driver.find_element(By.CSS_SELECTOR,"div>h1.entry-title").text)

elements=driver.find_elements(By.CSS_SELECTOR,"div.et_pb_blurb_description")
for ele in elements:
    print(ele.text)
print("Test Passed!!!!!!!!!!!!!!!!!!!!!")
