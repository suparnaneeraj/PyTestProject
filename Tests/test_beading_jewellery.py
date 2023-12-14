import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def setUp():
    global driver
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    #driver.quit()
    print("Test Completed")

def test_beading_jewellery(setUp):
    wait = WebDriverWait(driver, 20)
    driver.get("https://www.amazon.com")
    driver.find_element(By.ID, 'nav-hamburger-menu').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='hmenu-item']/div[text()='Arts & Crafts']"))).click()
    element=driver.find_element(By.XPATH, "//a[text()='Beading & Jewelry Making']")
    driver.execute_script("arguments[0].click();", element)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Arts, Crafts & Sewing']"))).click()
    driver.find_element(By.XPATH, "//span[@class='a-list-item']//span[text()='Beading & Jewelry Making']").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'Engraving Machines & Tools')]").click()
    driver.find_element(By.CSS_SELECTOR, "span.a-dropdown-label").click()
    driver.find_element(By.XPATH, "//a[text()='Price: High to Low']").click()
    driver.find_element(By.CSS_SELECTOR, "div[data-index='4']").click()
    review_score = driver.find_element(By.XPATH, "//span[@id='acrPopover']//span[@class='a-size-base a-color-base']").text.strip()
    assert float(review_score) >= 4
    product_price = driver.find_element(By.XPATH, "//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']/span[@class='a-offscreen']").get_attribute("innerText")
    print(product_price)
    amount = product_price[1:]
    print("The amount is", amount)
    assert float(amount.replace(",", "")) <= 4000


