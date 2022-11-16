import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.way2automation.com/way2auto_jquery/index.php")
print(driver.find_element(By.XPATH,"//h3[contains(text(),'Dummy')]").text)
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Ding3834934")
driver.find_element(By.NAME,"phone").send_keys("239829323923773")
driver.find_element(By.NAME,"email").send_keys("usewesd83038430483488348fgd.com")


# identify dropdown with Select class
#sel = Select(driver.find_element(By.XPATH,"//select[@name='continents']"))
#select by select_by_visible_text() method
#sel.select_by_visible_text("Europe")
time.sleep(2);

select=Select(driver.find_element((By.XPATH,"//select[@name='country']")))
select.select_by_visible_text("Ghana")
#select.select_by_index(2)

print("Reg Form test passed...!!!!")
