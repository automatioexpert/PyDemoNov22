from selenium import webdriver

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.get()
