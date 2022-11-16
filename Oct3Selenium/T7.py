import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.mindnode.com/")
driver.find_element(By.CSS_SELECTOR,"a[href*='about']").click()
time.sleep(3)
paras=driver.find_elements(By.CSS_SELECTOR,"div.about__header>p")
for para in paras:
    print(para.text)

driver.quit()
print('I am the Top Expert on the Planet in Python..Thank God!!!!')