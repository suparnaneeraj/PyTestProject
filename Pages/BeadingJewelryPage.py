from Pages.BasePage import BasePage
from Pages.EngravingMachinetools import EngravingMachinesToolsPage
from utilities.locators import BeadingJewelryMakingLocators, CommonLocators


class BeadingJewelryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def search_beading_jewelry(self, search_value):
        self.search(CommonLocators.search_box, search_value, CommonLocators.search_submit_button)

    def click_engraving_machine_tools(self):
        self.click(BeadingJewelryMakingLocators.engraving_machine_tools_menu)
        return EngravingMachinesToolsPage()
