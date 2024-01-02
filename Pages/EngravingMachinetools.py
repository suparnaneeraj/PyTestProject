from Pages.BasePage import BasePage
from utilities.locators import EngravingMachineToolsLocators, CommonLocators


class EngravingMachinesToolsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def sort_page_results(self, sorting_criteria):
        self.sort_results(CommonLocators.sort_by_dropdown, sorting_criteria)

    def click_on_third_product(self):
        self.click(EngravingMachineToolsLocators.select_third_product)

    def get_product_rating(self):
        if self.verify_if_element_present(EngravingMachineToolsLocators.product_rating):
            return self.get_text(EngravingMachineToolsLocators.product_rating)
        else:
            return "0"

    def get_product_price(self):
        return self.get_inner_text(EngravingMachineToolsLocators.product_price)
