from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html");

sel=Select(driver.find_element(By.XPATH,"//select[@id='course']"))
sel.select_by_visible_text("Java")
print("Selected Python from dropdown..!!")

