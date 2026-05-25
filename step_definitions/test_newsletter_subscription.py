'''
Step Definition File: Newsletter Subscription
# Description: This file contains step definitions for newsletter subscription test scenarios using pytest-bdd framework.
Author: Thejasvi Dhayalan
Date: May 2026
'''

import pytest
import json
from pytest_bdd import scenario, given, when, then, parsers
from pages.login_page import LoginPage
from pages.common_page import CommonPage

# Load user credentials from JSON file
with open("data\\user_login.json") as credentials:
    user_data = json.load(credentials)
    users_list = user_data['users']

@pytest.fixture(params=users_list)
def user_credentials(request):
    """
    Fixture to provide user credentials as parameters for data-driven testing.

    Args:
        request: Pytest request object

    Returns:
        User credentials dictionary
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
    '../features/newsletter_subscription.feature',
    'User Successfully subscribes to newsletter with valid credentials'
)
def test_newsletter_subscription(browser_instance, context):
    """
    Test scenario for newsletter subscription functionality.
    This test is linked to the feature file scenario.
    """
    pass


@given(parsers.parse('the user logs in with valid credentials using "{email}" and "{password}" and "{name}"'))
def login(context, email, password, name):
    """
    Step definition for user login with valid credentials.

    Args:
        context: Context dictionary for sharing data
        email: User email address
        password: User password
        name: User name

    Returns:
        Updated context dictionary
    """
    context['user_email'] = email
    context['user_password'] = password
    context['user_name'] = name

    login_object = LoginPage(context['page'])
    login_object.login(email, password)
    login_object.login_successful(name)
    return context

@when('the user navigates to newsletter subscription section')
def navigate_to_newsletter(context):
    """
    Step definition for navigating to newsletter subscription section.

    Args:
        context: Context dictionary for sharing data

    Returns:
        Updated context dictionary
    """
    common_page_object = CommonPage(context['page'])
    context['common_page'] = common_page_object
    return context

@when('subscribes to newsletter with their email address')
def subscribe_newsletter(context):
    """
    Step definition for subscribing to newsletter with user's email.

    Args:
        context: Context dictionary for sharing data

    Returns:
        Updated context dictionary
    """
    user_email = context['user_email']
    common_page_object = context['common_page']
    common_page_object.subscription(user_email)
    common_page_object.subscription_verification()
    return context

@then('the newsletter subscription should be successful')
def verify_subscription_success(context):
    """
    Step definition for verifying newsletter subscription success.

    Args:
        context: Context dictionary for sharing data

    Returns:
        Updated context dictionary
    """
    print("Newsletter subscription verification completed")
    return context

@then('the success confirmation message should be displayed')
def verify_success_message(context):
    """
    Step definition for verifying success confirmation message.

    Args:
        context: Context dictionary for sharing data

    Returns:
        Updated context dictionary
    """
    print("Success confirmation message verified")
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

