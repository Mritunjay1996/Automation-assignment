from selenium.webdriver.common.by import By
import allure


class HomePage:
    app_logo = (By.XPATH, '//div[@class="app_logo"]')
    cart_icon = (By.CSS_SELECTOR, 'a.shopping_cart_link')
    add_rmv_btn = (By.CSS_SELECTOR, 'button.btn_inventory')
    inventory_items = (By.CSS_SELECTOR, 'div.inventory_item')
    # product_title = '//div[@data-test="inventory-item-name"]'
    product_title = (By.CSS_SELECTOR, ".inventory_item_name")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Verify that the profile icon is displayed')
    def is_app_logo_displayed(self):
        return self.browser.find_element(*self.app_logo).is_displayed()

    @allure.step('Add first item to cart')
    def add_first_item_cart(self, item):
        add_button = self.browser.find_elements(*self.add_rmv_btn)[0]
        button_text = add_button.text

        if button_text == "Add to cart":
            self.add_item_to_cart(item)
            btnTxt = self.browser.find_elements(*self.add_rmv_btn)[0]
            assert btnTxt.text == 'Remove', "Button text did not change to 'Remove'"
        else:
            "item is already added to the cart"

    @allure.step('Add item to cart')
    def add_item_to_cart(self, item):
        self.browser.find_element(*self.add_cart_btn(item)).click()

    @allure.step('Click on cart icon')
    def click_cart_icon(self):
        self.browser.find_element(*self.cart_icon).click()

    @allure.step('Click on the first product item')
    def click_first_product(self):
        first_item_link = self.browser.find_elements(*self.product_title)[0]
        item_title = first_item_link.text
        first_item_link.click()
        return item_title

    def add_cart_btn(self, item):
        return (By.CSS_SELECTOR, f'#add-to-cart-sauce-labs-{item}')
