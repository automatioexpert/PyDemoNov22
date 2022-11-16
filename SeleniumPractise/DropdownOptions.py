
from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
options=driver.find_elements(By.CSS_SELECTOR,"select#course>option")
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html")
driver.find_element(By.XPATH,"//a[contains(text(),'Contact')]").click()
driver.find_element(By.CSS_SELECTOR,"input#ContactForm1_contact-form-email").send_keys("Useuer34374347348@gmail.coms")
print("I am the top expert on the Planet..Thank God!!!")
driver.close()


