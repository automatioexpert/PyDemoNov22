from E2E_Framework.Base import locatorReader, initializeDriver
from E2E_Framework.pages import GooglePage


def test_verifySearch():
    browser=initializeDriver.startBrowser("https://www.google.com")
    r=GooglePage.reg(browser)
    r.enterDataUsingName(locatorReader.readLocator("Registration","searchBox"))



