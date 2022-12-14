from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.nm.gov/")
driver.find_element(By.XPATH,"//a[contains(text(),'Online Services')]").click()
print(driver.find_element(By.CSS_SELECTOR,"div>h1.entry-title").text)
elements=driver.find_elements(By.CSS_SELECTOR,"li.agency-list-item>a")
for element in elements:
    print(element.text)
driver.quit()
print("Test case is Passed!!")