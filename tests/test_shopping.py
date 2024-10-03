import pytest
from pages.login import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from resources.variables import *
import allure

# Fixtures
@pytest.fixture
def login(browser):
    login_page = LoginPage(browser)
    login_page.open(URL)
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login_button()
    assert login_page.verify_successfulLogin() is True, "Login failed for valid user"
    return login_page


@pytest.fixture
def add_product_to_cart(browser, login):
    home_page = HomePage(browser)
    cart_page = CartPage(browser)
    home_page.add_first_item_cart(item_name)
    home_page.click_cart_icon()
    cart_page.verify_product_in_cart(item_name)


# Test Cases
@allure.title('TC_001: Verify user can successfully log in')
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


@allure.title('TC_003: Should add item from homepage to the cart ')
@pytest.mark.usefixtures("login")
def test_add_product_to_cart(browser):
    home_page = HomePage(browser)
    cart_page = CartPage(browser)
    home_page.add_first_item_cart(item_name)
    home_page.click_cart_icon()
    cart_page.verify_product_in_cart(item_name)


@allure.title('TC_004: Verify user can proceed to checkout')
@pytest.mark.usefixtures("add_product_to_cart")
def test_place_order(browser):
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)
    cart_page.proceed_to_checkout()
    assert checkout_page.verify_checkout_page() is True, "By clicking on checkout, it didn't proceed to the next steps"
    checkout_page.fill_checkout_details(first_name, last_name, post_code)
    checkout_page.place_order()
    checkout_page.click_finish_order()
