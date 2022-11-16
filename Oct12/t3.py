import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.cancer.gov/publications")
time.sleep(4)
driver.find_element(By.XPATH,"//a[contains(text(),'PDQ')]/following-sibling::button//span[contains(text(),'Expand')]").click()
tops=driver.find_elements(By.CSS_SELECTOR,"li.level-2.has-children>div>a")
for top in tops:
    print(top.text)

driver.quit()