'''
Test File: Invalid Login
Description: This test file contains test cases for invalid login functionality on the automation exercise website.
Author: Thejasvi Dhayalan
Date: May 2026
'''

import json
import pytest
from pages.login_page import LoginPage

pytestmark = pytest.mark.invalid_login

# Load invalid user credentials from JSON file
with open("data\\invalid_user_login.json") as credentials:
    user_data = json.load(credentials)
    users_list = user_data["invalid_users"]

@pytest.mark.parametrize("user_credentials", users_list)
def test_invalid_login(browser_instance, user_credentials):
    """
    Verify that user cannot login with invalid credentials.

    Args:
        browser_instance: Browser page instance from conftest
        user_credentials: Dictionary containing invalid login credentials
    """

    # Extract invalid user credentials
    user_email = user_credentials["invalid_user_email"]

    user_password = user_credentials["invalid_user_password"]

    # Create LoginPage object
    login_object = LoginPage(browser_instance)

    # Perform login with invalid credentials
    login_object.login(user_email, user_password)

    # Verify login failure message
    login_object.login_failed()

    