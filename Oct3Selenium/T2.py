from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.armymwr.com/m/privacy-policy")
print(driver.find_element(By.XPATH,"//h1").text);
driver.find_element(By.CSS_SELECTOR,"a.header-title.text-decoration-none").click()
driver.find_element(By.CSS_SELECTOR,"a[href*='sitemap']").click()
h4s=driver.find_elements(By.CSS_SELECTOR,"div h4")
for h4 in h4s:
    print(h4.text)
driver.quit()