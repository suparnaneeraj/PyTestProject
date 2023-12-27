from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(locator)

    def click(self, locator):
        self.find(locator).click()

    def get_text(self,locator):
        return self.find(locator).text

    def set_text(self,locator,value):
        self.find(locator).clear()
        self.find(locator).send_keys(value)

    def click_category(self,category_name):
        category = By.XPATH, "//div[@class='hmenu-item hmenu-title ' and text()='"+category_name+"']"
        self.click(category)

    def click_menu_from_category(self, menu_name):
        menu = By.XPATH, "//a[@class='hmenu-item']/div[text()='"+menu_name+"']"
        self.click(menu)

    def click_menu_inside_main_menu(self, menu_name):
        menu = By.XPATH, "//a[@class='hmenu-item' and text()='"+menu_name+"']"
        self.click(menu)

    def search(self,search_box_locator, value,search_button_locator):
        self.set_text(search_box_locator, value)
        self.click(search_button_locator)

    def sort_results(self,sort_dropdown_locator,sorting_criteria):
        self.click(sort_dropdown_locator)
        self.click(sorting_criteria)

    def get_inner_text(self,locator):
        return self.find(locator).get_attribute("innerText")