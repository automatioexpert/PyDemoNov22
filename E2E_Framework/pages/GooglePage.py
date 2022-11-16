class reg:
    def __init(self,focusFromPreviousHandle):
        global driver
        driver=focusFromPreviousHandle

    def enterDataUsingXpath(self,locator,data):
        driver.find_element_by_xpath(locator).send_keys(data)

    def enterDataUsingName(self,locator,data):
        driver.find_element_by_name(locator).send_keys(data)

    def enterDataUsingTagName(self, locator, data):
        driver.find_element_by_tagName(locator).send_keys(data)
