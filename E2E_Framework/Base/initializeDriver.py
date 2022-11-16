from selenium import webdriver

#chromedriver
driver=webdriver.Chrome(executable_path="../Driver/chromedriver.exe")


def startBrowser(url):
    """
    This is for starting the chrome browser
    :return: driver
    """
    driver.get(url)
    driver.maximize_window()
    return driver

def stopBrowser():
    driver.close()
    driver.quit()
