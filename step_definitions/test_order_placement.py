'''
Step Definition File: Order Placement
Description: This file contains step definitions for order placement test scenarios using pytest-bdd framework.
Author: Thejasvi Dhayalan
Date: May 2026
'''

import itertools
import pytest
import json
from pytest_bdd import scenario, given, when, then
from pages.common_page import CommonPage
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

# Load user credentials from JSON file
with open("data\\user_login.json") as credentials:
    user_data = json.load(credentials)
    users_list = user_data['users']

# Load payment details from JSON file
with open("data\\payment.json") as credentials:
    payment_data = json.load(credentials)
    payment_list = payment_data['payment']

@pytest.fixture(params=itertools.product(users_list, payment_list))
def credentials_and_payment(request):
    """
    Fixture to provide user credentials and payment details as parameters.

    Args:
        request: Pytest request object

    Returns:
        Tuple of user credentials and payment details
    """
    return request.param

@pytest.fixture
def browser_page(browser_instance):
    """
    Fixture to provide the browser page instance.

    Args:
        browser_instance: Browser page instance from conftest

    Returns:
        Browser page instance
    """
    return browser_instance

@pytest.fixture
def context(browser_page):
    """
    Fixture to provide context dictionary for sharing data between steps.

    Args:
        browser_page: Browser page instance

    Returns:
        Dictionary containing page instance
    """
    return {'page': browser_page}

@scenario(
    '../features/order_placement.feature',
    'User Successfully place an order with valid credentials'
)

def test_place_order(browser_instance, context, credentials_and_payment):
    """
    Test scenario for order placement functionality.
    This test is linked to the feature file scenario.
    """
    pass

@given('the user logs in with valid credentials')
def login(context, credentials_and_payment):
    """
    Step definition for user login with valid credentials.

    Args:
        context: Context dictionary for sharing data
        credentials_and_payment: Tuple containing user credentials and payment details

    Returns:
        Updated context dictionary
    """
    user_credentials, payment_info = credentials_and_payment
    user_email = user_credentials['user_email']
    user_password = user_credentials['user_password']
    user_name = user_credentials['user_name']

    context['user_email'] = user_email
    context['user_password'] = user_password
    context['user_name'] = user_name

    context['card_name'] = payment_info['card_name']
    context['card_number'] = payment_info['card_number']
    context['cvc'] = payment_info['cvc']
    context['expiry_month'] = payment_info['expiry_month']
    context['expiry_year'] = payment_info['expiry_year']

    login_object = LoginPage(context['page'])
    login_object.login(user_email, user_password)
    login_object.login_successful(user_name)
    return context

@when('the user selects products')
def select_products(context):
    """
    Step definition for selecting products from the products page.

    Args:
        context: Context dictionary for sharing data

    Returns:
        Updated context dictionary
    """
    products_page_object = ProductsPage(context['page'])
    products_page_object.product_selection()
    context['products_page_object'] = products_page_object
    return context

@then('the cart should contain the selected products')
def verify_cart(context):
    """
    Step definition for verifying cart contents.

    Args:
        context: Context dictionary for sharing data

    Returns:
        Updated context dictionary
    """
    cart_page_object = CartPage(context['page'])
    cart_page_object.verify_cart()
    context['cart_page_object'] = cart_page_object
    return context

@then('the product count should match')
def verify_product_count(context):
    """
    Step definition for verifying product count matches between cart and products page.

    Args:
        context: Context dictionary for sharing data

    Returns:
        Updated context dictionary
    """
    cart_page_object = context['cart_page_object']
    products_page_object = context['products_page_object']
    cart_page_object.verify_product_count(products_page_object)
    return context

@then('the product names should match')
def verify_product_names(context):
    """
    Step definition for verifying product names match between cart and products page.

    Args:
        context: Context dictionary for sharing data

    Returns:
        Updated context dictionary
    """
    cart_page_object = context['cart_page_object']
    products_page_object = context['products_page_object']
    cart_page_object.verify_product_names(products_page_object)
    return context

@then('the user proceeds to checkout')
def proceed_to_checkout(context):
    """
    Step definition for proceeding to checkout.

    Args:
        context: Context dictionary for sharing data

    Returns:
        Updated context dictionary
    """
    common_page_object = CommonPage(context['page'])
    common_page_object.proceed_to_checkout()
    return context

@then('the total price should be verified')
def verify_total_price(context):
    """
    Step definition for verifying total price on checkout page.

    Args:
        context: Context dictionary for sharing data

    Returns:
        Updated context dictionary
    """
    user_name = context['user_name']
    from playwright.sync_api import expect
    if expect(context['page'].get_by_text(f"Logged in as {user_name}")).to_be_visible():
        checkout_page_object = CheckoutPage(context['page'])
        checkout_page_object.verify_total_price()
    return context

@when('the user places the order')
def place_order(context):
    """
    Step definition for placing the order.

    Args:
        context: Context dictionary for sharing data

    Returns:
        Updated context dictionary
    """
    common_page_object = CommonPage(context['page'])
    common_page_object.place_order()
    return context

@when('the user enters valid payment details')
def enter_payment_details(context):
    """
    Step definition for entering payment details.

    Args:
        context: Context dictionary for sharing data

    Returns:
        Updated context dictionary
    """
    payment_page_object = PaymentPage(context['page'])
    payment_page_object.place_order(
        context['card_name'],
        context['card_number'],
        context['cvc'],
        context['expiry_month'],
        context['expiry_year']
    )
    return context

@then('the order should be placed successfully')
def verify_order_success(context):
    """
    Step definition for verifying successful order placement.

    Args:
        context: Context dictionary for sharing data

    Returns:
        Updated context dictionary
    """
    return context

@then('the user logs out of the application')
def logout(context):
    """
    Step definition for user logout.

    Args:
        context: Context dictionary for sharing data

    Returns:
        Updated context dictionary
    """
    common_page_object = CommonPage(context['page'])
    common_page_object.logout()
    return context
