from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
driver.refresh();
print("Rereshed the webpage")
driver.refresh();
    
driver.close()
