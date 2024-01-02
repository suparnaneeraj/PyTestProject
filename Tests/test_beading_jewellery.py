import time

from Pages.HomePage import HomePage
from Tests.base_test import BaseTest


class TestBeadingJewellery(BaseTest):
    def test_beading_jewellery_price(self):
        home_page = HomePage(self.driver)
        # time.sleep(10)
        home_page.click_all_menu()
        home_page.select_from_category("Arts & Crafts")
        beading_jewelry_page = home_page.select_from_menu("Beading & Jewelry Making")
        beading_jewelry_page.search_beading_jewelry("Engraving Machines and Tools")
        engraving_machines_tools_page = beading_jewelry_page.click_engraving_machine_tools()
        engraving_machines_tools_page.sort_page_results("Price: High to Low")
        engraving_machines_tools_page.click_on_third_product()
        product_rating = engraving_machines_tools_page.get_product_rating().strip()
        if product_rating == "0":
            print("There is no review score available for the product")
        else:
            assert float(product_rating) >= 4
        product_price = engraving_machines_tools_page.get_product_price()
        amount = product_price[1:]
        assert float(amount.replace(",", "")) <= 4000
