'''
Page Object: Products Page
Description: This page object class contains locators and methods for interacting with the products page of the automation exercise website.
Author: Thejasvi Dhayalan
Date: May 2026
'''

from playwright.sync_api import expect, TimeoutError
from pages.common_page import CommonPage
from pages.home_page import HomePage
from utils.screenshot import capture_screenshot

class ProductsPage:

    def __init__(self, page):
        """
        Initialize the ProductsPage object with a Playwright page instance.

        Args:
            page: Playwright page instance
        """

        self.page = page

        # PLocators for roduct elements
        self.product1 = self.page.locator(".productinfo").filter(has_text="Sleeves Printed Top - White")
        self.product2 = self.page.locator(".productinfo").filter(has_text="Colour Blocked Shirt – Sky Blue")

        # Store selected product details
        self.product_count = 0
        self.product_names = []

    def product_selection(self):
        """
        Select products from products page
        and add them to cart.
        """

        try:
            # Navigate to kids category tops section
            home_page_object = HomePage(self.page)
            home_page_object.kids_category_tops()

            # List of products to select
            products = [self.product1, self.product2]

            # Select and add products to cart
            for product in products:

                # Wait for product visibility
                product.wait_for(timeout=5000)

                expect(product).to_be_visible()

                # Extract product name
                product_name = product.locator("p").first.text_content()

                if not product_name:
                    raise ValueError("Product name is empty.")

                self.product_names.append(product_name.strip())

                # Hover over product
                product.hover()

                # Click add to cart button
                product.locator("a[class*='add-to-cart']").click()

            # Navigate to cart page
            common_page_object = CommonPage(self.page)
            common_page_object.view_cart()

            # Update product count
            self.product_count = len(self.product_names)

            # Capture success screenshot
            capture_screenshot(self.page, "products_added_to_cart")

        except TimeoutError:
            capture_screenshot(self.page, "product_load_timeout")
            raise TimeoutError("Product loading timed out." )

        except ValueError as e:
            capture_screenshot(self.page, "product_name_error")
            raise ValueError(str(e))

        except Exception as e:
            capture_screenshot(self.page, "product_selection_failed")
            raise Exception( f"Product selection failed: {str(e)}")

            