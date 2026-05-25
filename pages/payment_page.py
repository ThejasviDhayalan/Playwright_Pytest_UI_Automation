'''
Page Object: Payment Page
Description: This page object class contains locators and methods for interacting with the payment page of the automation exercise website.
Author: Thejasvi Dhayalan
Date: May 2026
'''

from playwright.sync_api import expect, TimeoutError
from utils.screenshot import capture_screenshot

class PaymentPage:

    def __init__(self, page):
        """
        Initialize the PaymentPage object with a Playwright page instance.

        Args:
            page: Playwright page instance
            payment_page: Page locators
        """

        self.page = page

        # Locators for Payment form elements
        self.card_name = self.page.locator("input[data-qa='name-on-card']")
        self.card_number = self.page.locator("input[data-qa='card-number']")
        self.cvc = self.page.locator("input[data-qa='cvc']")
        self.expiry_month = self.page.locator("input[data-qa='expiry-month']")
        self.expiry_year = self.page.locator("input[data-qa='expiry-year']")
        self.confirm_order = self.page.locator("button[data-qa='pay-button']")

        # Order placed success message locator
        self.order_placed_locator = self.page.locator("h2:has-text('Order Placed!')")

    def place_order(self, card_name, card_number, cvc, expiry_month, expiry_year):
        """
        Fill payment details and place order.

        Args:
            card_name: Name on the card
            card_number: Card number
            cvc: Card verification code
            expiry_month: Card expiry month
            expiry_year: Card expiry year
        """

        try:
            # Fill payment details
            self.card_name.fill(card_name)
            self.card_number.fill(card_number)
            self.cvc.fill(cvc)
            self.expiry_month.fill(expiry_month)
            self.expiry_year.fill(expiry_year)

            # Click confirm order button
            self.confirm_order.click()

            # Wait for success message
            self.order_placed_locator.wait_for(
                state="visible",
                timeout=5000
            )

            # Verify order placement success message
            expect(self.order_placed_locator).to_have_text("Order Placed!")

            # Capture success screenshot
            capture_screenshot(self.page, "order_placed_success")

        except TimeoutError:
            capture_screenshot(self.page, "order_timeout_error")
            raise TimeoutError("Order placement timed out.")

        except AssertionError as e:
            capture_screenshot(self.page, "order_verification_failed")
            raise AssertionError(f"Order verification failed: {str(e)}")

        except Exception as e:
            capture_screenshot(self.page, "order_placed_failure")
            raise Exception(f"Failed to place order: {str(e)}")
        
        