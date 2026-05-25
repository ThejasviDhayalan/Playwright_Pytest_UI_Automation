'''
Page Object: Contact Page
Description: This page object class contains locators and methods for interacting with the contact page of the automation exercise website.
Author: Thejasvi Dhayalan
Date: May 2026
'''

from playwright.sync_api import TimeoutError
from utils.screenshot import capture_screenshot

class ContactPage:

    def __init__(self, page):
        """
        Initialize the ContactPage object with a Playwright page instance.

        Args:
            page: Playwright page instance
            contact_page: Page locators
        """

        self.page = page

        # Locators for contact form elements
        self.contact_form_link = self.page.locator("a[href='/contact_us']")
        self.user_name = self.page.locator("input[data-qa='name']")
        self.user_email = self.page.locator("input[data-qa='email']")
        self.subject = self.page.locator("input[data-qa='subject']")
        self.message = self.page.locator("textarea[data-qa='message']")
        self.file_upload = self.page.locator("input[type='file']")
        self.submit_button = self.page.locator("input[type='submit']")

    def contact_form(self, user_name, user_email):
        """
        Fill and submit the contact form with user details.

        Args:
            user_name: Name of the user
            user_email: Email address of the user
        """

        try:
            # Navigate to contact form page
            self.contact_form_link.click()

            # Wait for form fields to load
            self.user_name.wait_for(timeout=5000)

            # Fill contact form details
            self.user_name.fill(user_name)
            self.user_email.fill(user_email)
            self.subject.fill("Test Subject")
            self.message.fill("Product review")

            # Upload attachment file
            file_path = "data\\contact_form.txt"
            self.file_upload.set_input_files(file_path)

            # Handle confirmation dialog
            self.page.once("dialog", lambda dialog: dialog.accept())

            # Submit contact form
            self.submit_button.click()

            # Capture success screenshot
            capture_screenshot(self.page, "contact_form_submitted")

        except FileNotFoundError:
            capture_screenshot(self.page, "contact_file_not_found")
            raise FileNotFoundError("Attachment file not found.")

        except TimeoutError:
            capture_screenshot(self.page, "contact_page_timeout")
            raise TimeoutError("Contact page elements not loaded within timeout." )

        except Exception as e:
            capture_screenshot(self.page, "contact_form_submission_failed")
            raise Exception(f"Contact form submission failed: {str(e)}")
        