'''
Test File: Order Placement
Description: This test file contains test cases for order placement functionality on the automation exercise website.
Author: Thejasvi Dhayalan
Date: May 2026 
'''

import itertools
import json
import pytest
from playwright.sync_api import Playwright, expect
from pages.common_page import CommonPage
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

pytestmark = pytest.mark.e2e

# Load user credentials from JSON file
with open("data\\user_login.json") as credentials:
    user_data = json.load(credentials)
    users_list = user_data["users"]

# Load payment details from JSON file
with open("data\\payment.json") as credentials:
    payment_data = json.load(credentials)
    payment_list = payment_data["payment"]

@pytest.mark.parametrize("user_credentials,payment_data", itertools.product(users_list, payment_list))
def test_02_order_placement(browser_instance, user_credentials, payment_data):
    """
    Test case for end-to-end order placement functionality.

    This test verifies the complete order flow from login to payment,
    including product selection, cart verification, checkout, and payment.

    Args:
        browser_instance: Browser page instance from conftest
        user_credentials: Dictionary containing user login credentials
        payment_data: Dictionary containing payment details
    """
    # Extract user credentials
    user_email = user_credentials["user_email"]
    user_password = user_credentials["user_password"]
    user_name = user_credentials["user_name"]

    # Extract payment details
    card_name = payment_data["card_name"]
    card_number = payment_data["card_number"]
    cvc = payment_data["cvc"]
    expiry_month = payment_data["expiry_month"]
    expiry_year = payment_data["expiry_year"]

    # Step 1: Login to the application
    login_object = LoginPage(browser_instance)
    login_object.login(user_email, user_password)
    login_object.login_successful(user_name)

    # Step 2: Select products from the products page
    products_page_object = ProductsPage(browser_instance)
    products_page_object.product_selection()

    # Step 3: Verify cart contents
    cart_page_object = CartPage(browser_instance)
    cart_page_object.verify_cart()
    cart_page_object.verify_product_count(products_page_object)
    cart_page_object.verify_product_names(products_page_object)

    # Step 4: Proceed to checkout
    common_page_object = CommonPage(browser_instance)
    common_page_object.proceed_to_checkout()

    # Step 5: Verify checkout details
    checkout_page_object = CheckoutPage(browser_instance)
    checkout_page_object.verify_total_price()

    # Step 6: Place the order
    common_page_object.place_order()

    # Step 7: Complete payment
    payment_page_object = PaymentPage(browser_instance)
    payment_page_object.place_order(card_name, card_number, cvc, expiry_month, expiry_year)

    # Step 8: Logout from the application
    common_page_object.logout()

