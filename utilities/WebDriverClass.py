import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utilities.TestData import TestData


class WebDriverClass:

    @pytest.fixture()
    def initialise_driver(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(TestData.url)
        yield
        print("Closing the driver")
        driver.quit()




