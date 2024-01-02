import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utilities.TestData import TestData


@pytest.fixture(scope="class")
def initialise_driver(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    driver.get(TestData.url)
    yield
    print("Closing the driver")
    driver.quit()
