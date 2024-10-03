from selenium.webdriver.common.by import By
import allure

class CartPage:
    """
    Define all web element locators and test steps
    for the cart page.
    """

    cart_icon = (By.XPATH, '//a[@data-test="shopping-cart-link"]')
    item_name = (By.CSS_SELECTOR, 'div.inventory_item_name')
    checkout_button = (By.XPATH, '//button[@id="checkout"]')

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Open the cart')
    def open_cart(self):
        self.browser.find_element(*self.cart_icon).click()

    @allure.step('Verify the added item in the cart')
    def verify_product_in_cart(self, product_name):
        # Assuming that cart items are listed in a table or a div, we will fetch all products in the cart
        items = self.browser.find_elements(*self.item_name)
        for item in items:
            if product_name.lower() in item.text.lower():
                return True
        return False

    @allure.step('Proceed to checkout')
    def proceed_to_checkout(self):
        self.browser.find_element(*self.checkout_button).click()

