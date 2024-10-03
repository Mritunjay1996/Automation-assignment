from selenium.webdriver.common.by import By
import allure


class LoginPage:
    """
    Define all web element locators and test steps
    in this class for the login page.
    """

    email_textbox = (By.XPATH, '//input[@id="user-name"]')
    login_button = (By.XPATH, '//input[@id="login-button"]')
    password_textbox = (By.XPATH, '//input[@id="password"]')
    inventory_list = (By.XPATH, '//div[@class="inventory_list"]')

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Open the login page')
    def open(self, url):
        self.browser.get(url)

    @allure.step('Enter Email in the email field')
    def enter_email(self, username):
        email_field = self.browser.find_element(*self.email_textbox)
        email_field.clear()
        email_field.send_keys(username)

    @allure.step('Enter Password in the password field')
    def enter_password(self, password):
        self.browser.find_element(*self.password_textbox).clear()
        self.browser.find_element(*self.password_textbox).send_keys(password)

    @allure.step('Proceed to the next step by clicking Next')
    def click_login_button(self):
        self.browser.find_element(*self.login_button).click()

    @allure.step('Verify user is logged in successfully')
    def verify_successfulLogin(self):
        try:
            return self.browser.find_element(*self.inventory_list).is_displayed()
        except:
            return False
