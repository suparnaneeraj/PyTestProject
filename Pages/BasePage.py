from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(*locator).click()

    def get_text(self, locator):
        return self.find(*locator).text

    def set_text(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def click_category(self, category_name):
        category = By.XPATH, "//div[@class='hmenu-item hmenu-title ' and text()='" + category_name + "']"
        self.click(category)

    def click_menu_from_category(self, menu_name):
        menu = By.XPATH, "//a[@class='hmenu-item']/div[text()='" + menu_name + "']"
        self.wait_for_element_clickable(menu)
        self.click(menu)

    def click_menu_inside_main_menu(self, menu_name):
        menu = By.XPATH, "//a[@class='hmenu-item' and text()='" + menu_name + "']"
        self.execute_javascript(menu)

    def search(self, search_box_locator, value, search_button_locator):
        self.set_text(search_box_locator, value)
        self.click(search_button_locator)

    def sort_results(self, sort_dropdown_locator, sorting_criteria):
        self.click(sort_dropdown_locator)
        self.click_sorting_criteria(sorting_criteria)

    def get_inner_text(self, locator):
        return self.find(*locator).get_attribute("innerText")

    def wait_for_element_clickable(self, *locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(*locator))

    def execute_javascript(self, locator):
        self.driver.execute_script("arguments[0].click();", self.find(*locator))

    def click_sorting_criteria(self, criteria):
        sorting_criteria_locator = By.XPATH, "//a[text()='" + criteria + "']"
        self.click(sorting_criteria_locator)

    def verify_if_element_present(self,locator):
        try:
            self.find(*locator)
        except NoSuchElementException:
            return False


