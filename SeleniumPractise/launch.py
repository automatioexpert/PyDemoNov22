from selenium import webdriver


def launch():
    driver = webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.google.com")
    print("I am the World Champion");
