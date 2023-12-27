from Pages.BasePage import BasePage
from Pages.BeadingJewelryPage import BeadingJewelryPage
from utilities.locators import HomePageLocators


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_all_menu(self):
        self.click(HomePageLocators.all_menu_icon)

    def select_from_category(self,menu_name):
        self.click_menu_from_category(menu_name)

    def select_from_menu(self,menu_name):
        self.click_menu_inside_main_menu(menu_name)
        return BeadingJewelryPage()












