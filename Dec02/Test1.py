from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.way2automation.com/way2auto_jquery/registration.php#load_box")

driver.find_element(By.NAME,"name").send_keys("user3743434774")
driver.find_element(By.XPATH,"//label[contains(text(),'Last')]/following-sibling::input").send_keys("Vishwa334347")
driver.find_element(By.XPATH," (//input[@name='m_status'])[2]").click()
driver.find_element(By.XPATH,"//div[@class='radio_wrap']/label[contains(text(),' Reading')]/input[@type='checkbox']").click()
driver.find_element(By.NAME,"phone").send_keys("3348348483843")
driver.find_element(By.NAME,"username").send_keys("user34934394")
driver.find_element(By.NAME,"email").send_keys("user3943444494@gmail.com")
driver.find_element(By.XPATH,"//input[@type='file']").send_keys("C:\\Users\\valmiki\\Desktop\\vv(3).png")
print("Test Passed!!")

