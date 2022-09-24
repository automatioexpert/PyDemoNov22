from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/valmiki/Desktop/Exe/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

#Verify the logo on the Login page
print(driver.find_element("xpath","//div[@class='login_logo']").is_displayed())
driver.find_element(By.CSS_SELECTOR,"input#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR,"div>input#password").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@name='login-button']").click();
driver.find_element(By.CSS_SELECTOR,"button#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR,"a.shopping_cart_link").click()
selected_item_name=driver.find_element(By.CSS_SELECTOR,"div.inventory_item_name").text;
print("Selected item in the cart is: ",selected_item_name)
driver.find_element(By.CSS_SELECTOR,"button#checkout").click()
driver.find_element(By.CSS_SELECTOR,"input#first-name").send_keys("Dinga Baliyari Ahra")
driver.find_element(By.CSS_SELECTOR,"input[name='lastName']").send_keys("Pinga Chanda Ahra")
driver.find_element(By.CSS_SELECTOR,"input#postal-code").send_keys("2382372937")
driver.find_element(By.CSS_SELECTOR,"input[name='continue']").click()
#print(driver.find_elements(By.CSS_SELECTOR,"div.summary_info_label")
driver.find_element(By.CSS_SELECTOR,"button#finish").click()
print("End to End testing for Sauce lab is completed..Thanks God!!!!")

print("Test case Passed..Thanks God!!")

#driver.close()
