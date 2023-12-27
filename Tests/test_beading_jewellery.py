from Pages.HomePage import HomePage
from Tests.base_test import BaseTest


class TestBeadingJewellery(BaseTest):
    def test_beading_jewellery_price(self):
        home_page = HomePage(self.driver)
        home_page.click_all_menu()
        home_page.select_from_category("Arts & Crafts")
        beading_jewelry_page = home_page.select_from_menu("Beading & Jewelry Making")
        beading_jewelry_page.search_beading_jewelry("Engraving Machines and Tools")
        engraving_machines_tools_page = beading_jewelry_page.click_engraving_machine_tools()
        engraving_machines_tools_page.sort_page_results("Price: High to Low")
        engraving_machines_tools_page.click_on_third_product()
        product_rating=engraving_machines_tools_page.get_product_rating().strip()
        print(product_rating)
        assert float(product_rating) >= 4
        # wait.until(
        #     EC.element_to_be_clickable((By.XPATH, "//a[@class='hmenu-item']/div[text()='Arts & Crafts']"))).click()
        # element = driver.find_element(By.XPATH, "//a[text()='Beading & Jewelry Making']")
        # driver.execute_script("arguments[0].click();", element)
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Arts, Crafts & Sewing']"))).click()

        product_price = engraving_machines_tools_page.get_product_price()
        print(product_price)
        amount = product_price[1:]
        print("The amount is", amount)
        assert float(amount.replace(",", "")) <= 4000
