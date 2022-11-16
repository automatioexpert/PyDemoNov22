import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.sugarcrm.com/au/request-demo/")

if driver.find_element(By.CSS_SELECTOR, "button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").is_displayed():
    {
driver.find_element(By.CSS_SELECTOR,"button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
}
driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys("usere3843499834@outlook.com")
driver.find_element(By.CSS_SELECTOR,"div#field29>input[type='checkbox']").click()
print(driver.get_cookies())

