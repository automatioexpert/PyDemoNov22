from selenium import webdriver
import pytest
import os
import sys

from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
# option.add_argument("headless")
option.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(executable_path="C:\\Users\\valmiki\Desktop\Exe\\chromedriver.exe", options=option)

driver.implicitly_wait(10)
driver.get("https://www.mindnode.com/")

ac = actionChains(driver);
