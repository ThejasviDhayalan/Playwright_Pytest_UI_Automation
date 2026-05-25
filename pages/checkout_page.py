'''
Page Object: Checkout Page
Description: This page object class contains locators and methods for interacting with the checkout page of the automation exercise website.
Author: Thejasvi Dhayalan
Date: May 2026
'''

from pages.common_page import CommonPage
from utils.screenshot import capture_screenshot

class CheckoutPage:

    def __init__(self, page):
        """
        Initialize the CheckoutPage object with a Playwright page instance.

        Args:
            page: Playwright page instance
            checkout_page: Page locators
        """

        self.page = page

        # Locator for individual product prices
        self.product_price = self.page.locator(".cart_price")
        # Locator for displayed total price
        self.total_price = self.page.locator(".cart_total_price").last

    def verify_total_price(self):
        """
        Verify that displayed total price matches
        the sum of individual product prices.
        """

        try:
            # Wait for product prices to load
            self.product_price.first.wait_for(timeout=5000)

            # Get all product price elements
            prices = self.product_price.all()

            calculated_total = 0

            # Calculate sum of all product prices
            for price_elem in prices:

                price_text = price_elem.text_content()

                if not price_text:
                    raise ValueError("Product price text is empty.")

                # Clean price text
                price_clean = (price_text.replace('Rs.', '').replace('Rs', '').replace(',', '').strip())

                # Convert cleaned value to float
                price = float(''.join(c for c in price_clean if c.isdigit() or c == '.'))

                calculated_total += price

            # Get displayed total price
            total_text = self.total_price.text_content()

            if not total_text:
                raise ValueError("Displayed total price is empty.")

            # Clean total price text
            total_clean = (total_text.replace('Rs.', '').replace('Rs', '').replace(',', '').strip())

            # Convert displayed total to float
            displayed_total = float(''.join(c for c in total_clean if c.isdigit() or c == '.'))

            # Verify calculated total matches displayed total
            assert abs(calculated_total - displayed_total) < 0.01, \
                f"Price mismatch! Sum: Rs {calculated_total}, Displayed: Rs {displayed_total}"

            print(f"Total price verified: Rs {displayed_total}")

            # Capture success screenshot
            capture_screenshot(self.page, "total_price_verified")

        except AssertionError as e:
            capture_screenshot(self.page, "price_mismatch")
            raise AssertionError(str(e))

        except ValueError as e:
            capture_screenshot(self.page, "invalid_price_format")
            raise ValueError(f"Price conversion failed: {str(e)}")

        except Exception as e:
            capture_screenshot(self.page, "checkout_verification_failed")
            raise Exception(f"Checkout verification failed: {str(e)}")
        
        