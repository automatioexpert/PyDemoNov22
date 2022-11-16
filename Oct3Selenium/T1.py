from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.armymwr.com/m/privacy-policy")
print(driver.find_element(By.XPATH,"//h1").text);

topics=driver.find_elements(By.CSS_SELECTOR,"dl.accordion>p")
for topic in topics:
    print(topic.text)

print("I am the best Expert on the Planet..Thank God!!")
driver.quit()