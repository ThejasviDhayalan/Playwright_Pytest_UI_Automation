'''
Test File: User Registration
Description: This test file contains test cases for user registration functionality on the automation exercise website.
Author: Thejasvi Dhayalan
Date: May 2026
'''

import pytest
import pandas as pd
from playwright.sync_api import Playwright
from pages.signup_page import SignUp

pytestmark = pytest.mark.registration

# Load test data from Excel file
df = pd.read_excel("data\\test_data.xlsx",
                   sheet_name="user_registration"
                   ).astype(str)

new_user_registration_list = df.to_dict(orient="records")

@pytest.mark.parametrize("new_user_registration_data", new_user_registration_list)
def test_01_new_user_registration(playwright: Playwright, browser_instance, new_user_registration_data):
    """
    Test case for new user registration functionality.

    This test verifies that a new user can successfully register on the website
    by filling out the registration form with valid details.

    Args:
        playwright: Playwright instance
        browser_instance: Browser page instance from conftest
        new_user_registration_data: Dictionary containing user registration details
    """
    # Extract user registration data from test data
    new_user_name = new_user_registration_data["NewUserName"]
    new_user_email = new_user_registration_data["NewUserEmail"]
    new_user_password = new_user_registration_data["Password"]
    card_days = new_user_registration_data["Days"]
    card_months = new_user_registration_data["Months"]
    card_years = new_user_registration_data["Years"]
    new_user_firstName = new_user_registration_data["FirstName"]
    new_user_lastName = new_user_registration_data["LastName"]
    new_user_company = new_user_registration_data["Company"]
    new_user_address1 = new_user_registration_data["Address1"]
    new_user_address2 = new_user_registration_data["Address2"]
    new_user_country = new_user_registration_data["Country"]
    new_user_state = new_user_registration_data["State"]
    new_user_city = new_user_registration_data["City"]
    new_user_zipcode = new_user_registration_data["Zipcode"]
    new_user_mobile_number = new_user_registration_data["MobileNumber"]

    # Initialize signup page object
    signup_page_object = SignUp(browser_instance)

    # Perform user registration with extracted data
    signup_page_object.signup(
        new_user_name, new_user_email, new_user_password, card_days, card_months, card_years,
        new_user_firstName, new_user_lastName, new_user_company, new_user_address1, new_user_address2,
        new_user_country, new_user_state, new_user_city, new_user_zipcode, new_user_mobile_number
    )
