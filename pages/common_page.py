'''
Page Object: Common Page
Description: This page object class contains common locators and methods used across multiple pages of the automation exercise website.
Author: Thejasvi Dhayalan
Date: May 2026
'''

from playwright.sync_api import expect
from utils.screenshot import capture_screenshot

class CommonPage:

    def __init__(self, page):
        """
        Initialize the CommonPage object with a Playwright page instance.

        Args:
            page: Playwright page instance
            common_page: Page locators
        """
        self.page = page

        # Common navigation locators
        self.signup_login_link_locator = self.page.get_by_role("link", name=" Signup / Login")
        self.view_cart_locator = self.page.get_by_role("link", name="View Cart")
        self.continue_shopping_locator = self.page.get_by_text("Continue Shopping")
        self.proceed_to_checkout_locator = self.page.locator(".check_out")
        self.place_order_locator = self.page.get_by_role("link", name="Place Order")
        self.logout_locator = self.page.get_by_role("link", name=" Logout")
        # Newsletter subscription locators
        self.subscription_locator = self.page.locator("#susbscribe_email")
        self.subscribe_locator = self.page.locator("#subscribe")

    def signup_login_link(self):
        """
        Click on the Signup / Login link.
        """
        self.signup_login_link_locator.click()

    def view_cart(self):
        """
        Click on the View Cart link.
        """
        self.view_cart_locator.click()

    def continue_shopping(self):
        """
        Click on the Continue Shopping button.
        """
        self.continue_shopping_locator.click()

    def proceed_to_checkout(self):
        """
        Click on the Proceed to Checkout button.
        """
        self.proceed_to_checkout_locator.click()

    def place_order(self):
        """
        Click on the Place Order link.
        """
        self.place_order_locator.click()

    def logout(self):
        """
        Click on the Logout link.
        """
        self.logout_locator.click()

    def subscription(self, user_email):
        """
        Subscribe to newsletter with the provided email address.

        Args:
            user_email: Email address to subscribe with
        """
        self.subscription_locator.fill(user_email)
        self.subscribe_locator.click()

    def subscription_verification(self):
        """
        Verify that the newsletter subscription was successful.
        """
        expect(self.page.get_by_text("You have been successfully subscribed!")).to_be_visible()
        capture_screenshot(self.page, "Newsletter subscription successful")
