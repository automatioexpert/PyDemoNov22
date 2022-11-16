from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.cancer.gov/publications")

topics=driver.find_elements(By.CSS_SELECTOR,"p a")

for top in topics:
    print(top.text)

print('I am the best expert on the Planet')
driver.close()