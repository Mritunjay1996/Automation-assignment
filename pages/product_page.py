from selenium.webdriver.common.by import By
import allure


class ProductPage:
    product_list = (By.XPATH, "//div[contains(@class,'product-item')]")
    add_to_cart_button = (By.XPATH, "//button[contains(text(),'Add to Cart')]")
    product_details = (By.CSS_SELECTOR, '.inventory_details_container')
    back_arrow = (By.XPATH, '//button[@id="back-to-products"]')

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Select a product from the product list')
    def select_product(self):
        self.browser.find_element(*self.product_list).click()

    @allure.step('Add the product to the cart')
    def add_product_to_cart(self):
        self.browser.find_element(*self.add_to_cart_button).click()

    @allure.step('Verify the product details page')
    def is_product_details_displayed(self):
        try:
            product_details_element = self.browser.find_element(*self.product_details)
            return product_details_element.is_displayed()
        except:
            return False

    @allure.step('Get item name displayed on the details page')
    def get_item_name_on_details_page(self, item):
        assert self.browser.find_element(*self.item_details_name(item)).is_displayed()

    @allure.step('click on back arrow button to redirect on homepage')
    def click_back_to_products(self):
        self.browser.find_element(*self.back_arrow).click()

    def item_details_name(self, item):
        return By.XPATH, f'//div[@data-test="inventory-item-name" and contains(text(),"{item}")]'
