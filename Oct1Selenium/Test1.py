
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.selenium.dev/documentation/webdriver/")
status=driver.find_element(By.CSS_SELECTOR,"span.navbar-logo").is_displayed()
print(status)
docs=driver.find_element(By.XPATH,"//span[contains(text(),'Documentation')]").text
print(docs)

#Print all the Header links

elements=driver.find_elements(By.CSS_SELECTOR,"a.nav-link")

print("Total Headers are : ",len(elements))
for element in elements:
    print(element.text)

print("Test Passed..I am the Passed")

driver.close()