from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.nm.gov/online-services/")
driver.find_element(By.XPATH,"//a[contains(text(),'Elected Officials')]").click()
elements=driver.find_elements(By.CSS_SELECTOR,"div.et_pb_team_member_description>h2")

for ele in elements:
    print(ele.text)
driver.quit()