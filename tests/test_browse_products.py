import time
import pytest
from pages.login import LoginPage
from pages.product_page import ProductPage
from pages.home_page import HomePage
from resources.variables import *
import allure


@pytest.fixture
def login_valid_user(browser):
    login_page = LoginPage(browser)
    login_page.open(URL)
    login_page.enter_email(email)  # Valid email
    login_page.enter_password(password)  # Valid password
    login_page.click_login_button()
    assert login_page.verify_successfulLogin() is True, "Login failed for valid user"
    return login_page


@allure.title('TC_001: Verify user can log in with invalid credentials, then valid credentials')
@pytest.mark.parametrize("username, passwrd", [(invalid_email, invalid_password), (email, password)])
def test_login(browser, username, passwrd):
    login_page = LoginPage(browser)
    login_page.open(URL)
    login_page.enter_email(username)
    login_page.enter_password(passwrd)
    login_page.click_login_button()
    if username == email:
        assert login_page.verify_successfulLogin() is True, "Login failed for valid user"
    else:
        assert login_page.verify_successfulLogin() is False, "Invalid user should not log in"


@allure.title('TC_002: Should be able to browse items after successful login')
def test_browse_items_after_login(browser, login_valid_user):
    home_page = HomePage(browser)
    product_page = ProductPage(browser)
    item_title = home_page.click_first_product()
    product_page.get_item_name_on_details_page(item_title)
    product_page.click_back_to_products()
