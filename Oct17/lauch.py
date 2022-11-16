from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
# option.add_argument("headless")
option.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(executable_path = "C:\\Users\\valmiki\Desktop\Exe\\chromedriver.exe", options=option)

driver.implicitly_wait(10)
driver.get("https://www.ferrari.com/en-IN")
print(driver.title)

elements = driver.find_elements(By.CSS_SELECTOR, "ul.Footer__nav-links__2veW6pMl>li")
for el in elements:
    print(el.text)

print("I am the Top expert on the Planet..Thank God")
driver.quit()
