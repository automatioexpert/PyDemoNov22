import os

from selenium.webdriver.chrome import webdriver

path=os.path.abspath('..')+"//Driver//chromedriver.exe"
print(path) #C:\Users\valmiki\PycharmProjects\PythonSelenium\pythonProject24Sep

driver = webdriver.Chrome(executable_path=path)

"""
C:\Users\valmiki\pythonProject24Sep\Scripts\python.exe C:/Users/valmiki/PycharmProjects/PythonSelenium/pythonProject24Sep/Dec04/t4.py 
C:\Users\valmiki\PycharmProjects\PythonSelenium\pythonProject24Sep//Driver//chromedriver.exe
Traceback (most recent call last):
  File "C:\Users\valmiki\PycharmProjects\PythonSelenium\pythonProject24Sep\Dec04\t4.py", line 8, in <module>
    driver=webdriver.Chrome(executable_path=path)
AttributeError: module 'selenium.webdriver.chrome.webdriver' has no attribute 'Chrome'
"""