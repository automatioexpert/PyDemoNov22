from selenium import webdriver;
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://acumenacademy.org/contact/")
driver.find_element(By.CSS_SELECTOR,"a[href*='part']").click()
print(driver.find_element(By.CSS_SELECTOR,"div p").text)
print('I am the best expert on the Planet')
driver.quit()