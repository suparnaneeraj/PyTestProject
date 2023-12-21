class BasePage:

    def __int__(self,driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.find(*locator).click()

    def get_text(self,*locator):
        return self.find(*locator).text
