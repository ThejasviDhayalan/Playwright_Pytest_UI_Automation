'''
Page Object: Login Page
Description: This page object class contains locators and methods for interacting with the login page of the automation exercise website.
Author: Thejasvi Dhayalan
Date: May 2026
'''

from playwright.sync_api import expect, TimeoutError
from pages.common_page import CommonPage
from utils.screenshot import capture_screenshot

class LoginPage:

    def __init__(self, page):
        """
        Initialize the LoginPage object with a Playwright page instance.

        Args:
            page: Playwright page instance
            login_page: Page locators
        """

        self.page = page

        # Locators for login form elements
        self.login_email_address = self.page.get_by_placeholder("Email Address").first
        self.login_password = self.page.get_by_placeholder("Password")
        self.login_button = self.page.get_by_role("button", name="Login")

    def login(self, user_email, user_password):
        """
        Perform login action using valid or invalid credentials.

        Args:
            user_email: User email address
            user_password: User password
        """

        try:
            # Navigate to signup/login page
            common_page_object = CommonPage(self.page)
            common_page_object.signup_login_link()

            # Wait for login email field to be visible
            self.login_email_address.wait_for(timeout=5000)

            # Fill login credentials
            self.login_email_address.fill(user_email)
            self.login_password.fill(user_password)

            # Click login button
            self.login_button.click()

        except TimeoutError:
            capture_screenshot(self.page, "login_timeout_error")
            raise Exception("Login failed due to timeout issue.")

        except Exception as e:
            capture_screenshot(self.page, "login_exception")
            raise Exception(f"Unexpected error during login: {str(e)}")

    def login_successful(self, user_name):
        """
        Verify successful login by validating logged-in username.

        Args:
            user_name: Expected username after successful login
        """

        try:
            # Verify logged-in username is displayed
            expect(self.page.get_by_text(f"Logged in as {user_name}")).to_be_visible(timeout=5000)

            # Capture success screenshot
            capture_screenshot(self.page, "successful_login")

        except Exception as e:
            capture_screenshot(self.page, "login_verification_failed")
            raise Exception(f"Login verification failed: {str(e)}")

    def login_failed(self):
        """
        Verify unsuccessful login by validating error message.
        """

        try:
            # Verify invalid login error message
            expect(self.page.get_by_text("Your email or password is incorrect!")).to_be_visible(timeout=5000)

            # Capture failure screenshot
            capture_screenshot(self.page, "failed_login")

        except Exception as e:
            capture_screenshot(self.page, "failed_login_verification_error")
            raise Exception(f"Failed login message not displayed: {str(e)}")
        
        