from selenium.webdriver.common.by import By
import time
import allure


class CheckoutPage:
    first_name = (By.XPATH, '//input[@id="first-name"]')
    last_name = (By.XPATH, '//input[@id="last-name"]')
    postal_code = (By.XPATH, '//input[@id="postal-code"]')
    place_order_button = (By.XPATH, '//input[@id="continue"]')
    finish_button = (By.XPATH, '//button[@data-test="finish"]')
    order_confirmation = (By.XPATH, '//div[@class="checkout_complete_container"]')
    checkout_page = (By.XPATH, '//div[@class="checkout_info_container"]')

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Fill in billing details')
    def fill_checkout_details(self, fname, lname, post_code):
        self.browser.find_element(*self.first_name).send_keys(fname)
        self.browser.find_element(*self.last_name).send_keys(lname)
        self.browser.find_element(*self.postal_code).send_keys(post_code)

    @allure.step('Place the order')
    def place_order(self):
        self.browser.find_element(*self.place_order_button).click()

    @allure.step('Confirm the order placing by clicking on finish button')
    def click_finish_order(self):
        self.browser.find_element(*self.finish_button).click()

    @allure.step('Verify order confirmation')
    def verify_order_confirmation(self):
        return self.browser.find_element(*self.order_confirmation).is_displayed()

    @allure.step('Verify that checkout page is displayed')
    def verify_checkout_page(self):
        return self.browser.find_element(*self.checkout_page).is_displayed()
