import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.oracle.com/")
# Now set the cookie. This one's valid for the entire domain
cookie = {"name": "foo", "value": "bar"}
driver.add_cookie(cookie)

# And now output all the available cookies for the current URL
ls = driver.get_cookies()
for l in ls:
    print(l)
