from selenium import webdriver;
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://acumenacademy.org/contact/")
print(driver.find_element(By.XPATH, "//p[contains(text(),'Radical')]").text)
print(driver.find_element(By.CSS_SELECTOR, "p.p4").text)
elements = driver.find_elements(By.XPATH, "//span[contains(text(),'For questions about')]")
for e in elements:
    print(e.text)

print("Thank You God for supporting me in my journey!!")
driver.quit()


