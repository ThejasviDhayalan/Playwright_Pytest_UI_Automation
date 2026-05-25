'''
Page Object: Sign Up Page
Description: This page object class contains locators and methods for interacting with the sign up page of the automation exercise website.
Author: Thejasvi Dhayalan
Date: May 2026
'''

from playwright.sync_api import expect, TimeoutError
from utils.screenshot import capture_screenshot

class SignUp:

    def __init__(self, page):
        """
        Initialize the SignUp object with a Playwright page instance.

        Args:
            page: Playwright page instance
        """

        self.page = page

        # Locators for Signup form elements
        self.signup_link = self.page.get_by_role("link",name=" Signup / Login")
        self.new_user_name = self.page.locator("input[data-qa='signup-name']" )
        self.new_user_email = self.page.locator( "input[data-qa='signup-email']")
        self.user_name_displayed = self.page.locator("#name")
        self.signup_button = self.page.locator("button[data-qa='signup-button']" )

        # Locators for Account creation form elements
        self.new_user_password = self.page.locator("#password")
        self.card_days = self.page.locator("#days")
        self.card_months = self.page.locator("#months")
        self.card_years = self.page.locator("#years")
        self.newsletter = self.page.locator("#newsletter")
        self.new_user_option = self.page.locator("#optin")
        self.new_user_firstName = self.page.locator("#first_name")
        self.new_user_lastName = self.page.locator("#last_name")
        self.new_user_company = self.page.locator("#company")
        self.new_user_address1 = self.page.locator("#address1")
        self.new_user_address2 = self.page.locator("#address2")
        self.new_user_country = self.page.locator("#country")
        self.new_user_state = self.page.locator("#state")
        self.new_user_city = self.page.locator("#city")
        self.new_user_zipcode = self.page.locator("#zipcode")
        self.new_user_mobile_number = self.page.locator("#mobile_number")
        self.new_user_create_account = self.page.locator("button[data-qa='create-account']")

    def signup(self,new_user_name,NewUserEmail,Password,Days,Months,Years,FirstName,LastName,Company,Address1,Address2,Country,State,City,Zipcode, MobileNumber):
        """
        Fill signup form and create a new account.

        Args:
            new_user_name: User name
            NewUserEmail: User email
            Password: User password
            Days: Birth day
            Months: Birth month
            Years: Birth year
            FirstName: First name
            LastName: Last name
            Company: Company name
            Address1: Primary address
            Address2: Secondary address
            Country: Country
            State: State
            City: City
            Zipcode: Postal code
            MobileNumber: Mobile number
        """

        try:
            # Navigate to signup page
            self.signup_link.click()

            # Fill initial signup form
            self.new_user_name.fill(new_user_name)
            self.new_user_email.fill(NewUserEmail)

            expect(self.signup_button).to_be_visible()

            self.signup_button.click()

            # Verify username displayed
            expect(
                self.user_name_displayed
            ).to_have_value(new_user_name)

            # Fill account creation form
            self.new_user_password.fill(Password)

            self.card_days.select_option(Days)
            self.card_months.select_option(Months)
            self.card_years.select_option(Years)

            self.newsletter.check()
            self.new_user_option.check()

            self.new_user_firstName.fill(FirstName)
            self.new_user_lastName.fill(LastName)
            self.new_user_company.fill(Company)

            self.new_user_address1.fill(Address1)
            self.new_user_address2.fill(Address2)

            self.new_user_country.select_option(Country)

            self.new_user_state.fill(State)
            self.new_user_city.fill(City)
            self.new_user_zipcode.fill(Zipcode)

            self.new_user_mobile_number.fill(MobileNumber)

            # Create account
            self.new_user_create_account.click()

            # Verify account creation success
            expect( self.page.get_by_text("Account Created!")).to_be_visible(timeout=5000)

            # Capture success screenshot
            capture_screenshot(self.page, "account_created_success")

        except TimeoutError:
            capture_screenshot( self.page,"signup_timeout_error" )
            raise TimeoutError("Signup process timed out." )

        except AssertionError as e:
            capture_screenshot(self.page,"signup_assertion_failed")
            raise AssertionError(f"Signup verification failed: {str(e)}")

        except Exception as e:
            capture_screenshot(self.page,"signup_failed")
            raise Exception(f"Signup process failed: {str(e)}")
        
        