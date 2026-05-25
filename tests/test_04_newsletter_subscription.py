'''
Test File: Newsletter Subscription
# Description: This test file contains test cases for newsletter subscription functionality on the automation exercise website.
Author: Thejasvi Dhayalan
Date: May 2026
'''

import pytest
import json
from playwright.sync_api import Playwright
from pages.login_page import LoginPage
from pages.common_page import CommonPage

pytestmark = pytest.mark.subscription

# Load user credentials from JSON file
with open("data\\user_login.json") as credentials:
    user_data = json.load(credentials)
    users_list = user_data["users"]

@pytest.mark.parametrize("user_credentials", users_list)
def test_04_newsletter_subscription(playwright: Playwright, browser_instance, user_credentials):
    """
    Test case for newsletter subscription functionality.

    This test verifies that a logged-in user can successfully subscribe
    to the newsletter with their email address.

    Args:
        playwright: Playwright instance
        browser_instance: Browser page instance from conftest
        user_credentials: Dictionary containing user login credentials
    """
    # Extract user credentials
    user_email = user_credentials["user_email"]
    user_password = user_credentials["user_password"]
    user_name = user_credentials["user_name"]

    # Step 1: Login to the application
    login_object = LoginPage(browser_instance)
    login_object.login(user_email, user_password)
    login_object.login_successful(user_name)

    # Step 2: Subscribe to newsletter and verify
    common_page_object = CommonPage(browser_instance)
    common_page_object.subscription(user_email)
    common_page_object.subscription_verification()

    # Step 3: Logout from the application
    common_page_object.logout()

