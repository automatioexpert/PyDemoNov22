from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html")

#Mouse Hover

source=driver.find_element(By.XPATH,"//a[contains(text(),'YouTube Courses')]")
english=driver.find_element(By.XPATH,"//a[contains(text(),'English')]")
apachePOI=driver.find_element(By.XPATH,"//a[contains(text(),'Apache POI')]")

action=ActionChains(driver)
action.move_to_element(source).move_to_element(english).click(apachePOI).perform()

paras=driver.find_elements(By.CSS_SELECTOR,"div.post-body.entry-content>p")

for par in paras:
    print(par.text)

print("Mouse hover test passed!!")



