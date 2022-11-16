
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/valmiki/Desktop/Exe/chromedriver.exe")
driver.maximize_window()
driver.get("https://about.google/")
parentWindow=driver.current_window_handle
print("parentWindow: "+parentWindow)
driver.find_element(By.CSS_SELECTOR,"a[href*='blog']").click()

allHandles=driver.window_handles
print(allHandles)

for handle in allHandles:
    if handle!=parentWindow:
        driver.switch_to.window(handle)
        driver.find_element(By.XPATH,"//a[contains(text(),'Company news')]").click()


driver.switch_to.window(parentWindow)
print(driver.find_element(By.CSS_SELECTOR,"section.module-anchor-statement.center.module-anchor-statement__header-one>div>h1").text)
driver.quit()
print("I am the Top Expert on the Planet..Thank God!!!")