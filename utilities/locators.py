from selenium.webdriver.common.by import By


class HomePageLocators:
    all_menu_icon = (By.ID, "nav-hamburger-menu")


class AllMenuLocators:
    arts_and_crafts_menu = (By.XPATH, "//a[@class='hmenu-item']/div[text()='Arts & Crafts']")
    beading_jewelry_menu = (By.XPATH, "//a[text()='Beading & Jewelry Making']")


# class BeadingJewelry:
#     shipping_arts_crafts_menu=(By.XPATH, "//span[text() = 'International Shipping Arts & Crafts']")
#
#
# class ArtsAndCrafts:
#     beading_jewelry_menu= (By.XPATH, "//span[text()='Beading & Jewelry Making']")


class BeadingJewelryMakingLocators:
    search_box = (By.ID, "twotabsearchtextbox")
    search_submit_button = (By.ID, "nav-search-submit-button")
    engraving_machine_tools_menu = (By.XPATH, "//span[contains(text(),'Engraving Machines & Tools')]")


class EngravingMachineToolsLocators:
    sort_by_dropdown = (By.CSS_SELECTOR, "span.a-dropdown-label")
    sort_by_price_high_to_low = (By.XPATH, "//a[text()='Price: High to Low']")
    select_third_product = (By.CSS_SELECTOR, "div[data-index='4']")
    product_rating = (By.XPATH, "//span[@id='acrPopover']//span[@class='a-size-base a-color-base']")
    product_price = (By.XPATH, "//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']/span[@class='a-offscreen']")