import pytest


@pytest.mark.usefixtures("initialise_driver")
class BaseTest:
    def get_driver(self):
        return self.driver
