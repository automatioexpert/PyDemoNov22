'''
Created on May 21, 2018

@author: vv
'''
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")

driver.get('https://www.w3.org/')
for a in driver.find_elements(By.XPATH,'.//a'):
    print(a.get_attribute('href'))

driver.close()
