'''
Page Object: Cart Page
Description: This page object class contains locators and methods for interacting with the cart page of the automation exercise website.
Author: Thejasvi Dhayalan
Date: May 2026
'''

from utils.screenshot import capture_screenshot

class CartPage:

    def __init__(self, page):
        """
        Initialize the CartPage object with a Playwright page instance.

        Args:
            page: Playwright page instance
            cart_page: Page locators
        """

        self.page = page

        # Locator for all product rows in cart table
        self.products = self.page.locator("tbody tr")

        # List to store cart product names
        self.cart_product_names = []

        # Variable to store cart product count
        self.cart_product_count = 0

    def verify_cart(self):
        """
        Verify cart contents and extract product names and count.
        """

        try:
            # Wait for cart products to load
            self.products.first.wait_for(timeout=5000)

            # Get all product rows from cart
            products_in_cart = self.products.all()

            # Store cart product count
            self.cart_product_count = len(products_in_cart)

            # Extract product names from cart
            for product_row in products_in_cart:

                product_name = product_row.locator("a[href*='/product_details']").text_content()

                if product_name:
                    self.cart_product_names.append(product_name.strip())

            # Capture screenshot after successful cart verification
            capture_screenshot(self.page, "cart_verified")

        except Exception as e:
            capture_screenshot(self.page, "cart_verification_failed")
            raise Exception(f"Cart verification failed: {str(e)}")

    def verify_product_count(self, products_page):
        """
        Verify that cart product count matches products page count.

        Args:
            products_page: ProductsPage instance containing selected product count
        """

        try:
            # Verify product count
            assert self.cart_product_count == products_page.product_count, \
                f"Count mismatch! Cart: {self.cart_product_count}, ProductsPage: {products_page.product_count}"

            print(f"Product count verified: {self.cart_product_count}")

        except AssertionError as e:
            capture_screenshot(self.page, "product_count_mismatch")
            raise AssertionError(str(e))

        except Exception as e:
            capture_screenshot(self.page, "product_count_verification_failed")
            raise Exception(f"Product count verification failed: {str(e)}")

    def verify_product_names(self, products_page):
        """
        Verify that cart product names match selected products.

        Args:
            products_page: ProductsPage instance containing selected product names
        """

        try:
            # Verify each selected product exists in cart
            for product_name in products_page.product_names:

                assert product_name in self.cart_product_names, \
                    f"Product '{product_name}' not found in cart!"

            print(f"Product names verified: {products_page.product_names}")

        except AssertionError as e:
            capture_screenshot(self.page, "product_name_mismatch")
            raise AssertionError(str(e))

        except Exception as e:
            capture_screenshot(self.page, "product_name_verification_failed")
            raise Exception(f"Product name verification failed: {str(e)}")
        