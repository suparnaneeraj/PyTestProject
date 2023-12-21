from Pages.BasePage import BasePage
from utilities.locators import HomePageLocators


class HomePage(BasePage):
    def __int__(self,driver):
        self.driver = driver

    def click_all_menu(self):
        self.click(HomePageLocators.all_menu_icon)







