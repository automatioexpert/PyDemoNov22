import configparser

def readLocator(section,key):
    reader=configparser.ConfigParser()
    reader.read("C:\\Users\\valmiki\\PycharmProjects\\PythonSelenium\\pythonProject24Sep\\E2E_Framework\\configData\\locators.cfg")
    return reader.get(section,key)

a=readLocator("Registration","searchBox")
print(a)


