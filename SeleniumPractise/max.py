from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
driver.maximize_window()
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
driver.fullscreen_window()
print("Full Screen window launched")
driver.minimize_window()
driver.fullscreen_window()

driver.quit()