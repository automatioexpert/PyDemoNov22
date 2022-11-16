import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\valmiki\\Desktop\\Exe\\chromedriver.exe")
#driver.timeouts.implicit_wait(10)
driver.maximize_window()
driver.get("https://www.selenium.dev/documentation/webdriver/")
h1=driver.find_element(By.XPATH,"//h1").text
print(h1)
h1=driver.find_element(By.XPATH,"//h1/following-sibling::div").text
print(h1)
ps=driver.find_elements(By.CSS_SELECTOR,"div.td-content>p")
#print("Length of para : "+len(ps))
for p in ps:
    print(p.text)

driver.find_element(By.CSS_SELECTOR,"a[href*='documentation']").click()
print(driver.find_element(By.XPATH,"//h1").text)

contents=driver.find_elements(By.CSS_SELECTOR,"div.td-content>p")
for content in contents:
    print(content.text)

driver.find_element(By.CSS_SELECTOR,"li>a[href*='project']").click()
print(driver.find_element(By.XPATH,"//h1").text)

h2=driver.find_elements(By.XPATH,"//h2")
for h in h2:
    print(h.text)

print("================================")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"span.DocSearch-Button-Placeholder").click()
driver.find_element(By.CSS_SELECTOR,"input#docsearch-input").send_keys("Selenium WebDriver")

driver.find_element(By.CSS_SELECTOR,"button[aria-label='Clear the query']").click()
driver.find_element(By.CSS_SELECTOR,"input#docsearch-input").send_keys("Selenium Grid")
time.sleep(3)
results=driver.find_elements(By.CSS_SELECTOR,"span.DocSearch-Hit-title")
for result in results:
    print(result.text.lower().__contains__("grid"))
print("I am the World Champion!!")

driver.close()





