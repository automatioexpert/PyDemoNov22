from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdrivermanager.chrome import ChromeDriverManager
#
# options = Options()
# options.add_argument("start-maximized")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://www.google.com")

driver=webdriver.Chrome(ChromeDriverManager().download_and_install())
driver.maximize_window()
driver.get("https://www.google.com")
