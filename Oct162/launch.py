from selenium import webdriver

option=webdriver.ChromeOptions()
option.add_argument("--start-maximized")
option.add_argument("headless")
option.add_argument("--ignore-certificate-errors")
driver=webdriver.Chrome(executable_path = "C:\\Users\\valmiki\Desktop\Exe\\chromedriver.exe",options=option)

driver.get("https://www.google.com")
print(driver.title)
driver.quit()