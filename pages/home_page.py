'''
Page Object: Home Page
Description: This page object class contains locators and methods for interacting with the home page of the automation exercise website.
Author: Thejasvi Dhayalan
Date: May 2026
'''

class HomePage:

    def __init__(self, page):
        """
        Initialize the HomePage object with a Playwright page instance.

        Args:
            page: Playwright page instance
            home_page: Page locators
        """
        self.page = page

        # Women category locators
        self.women_category = self.page.get_by_role("link", name = "Women")
        self.women_dress = self.page.get_by_role("link", name = "Dress ")
        self.women_tops = self.page.get_by_role("link", name = "Tops ")
        self.women_sarees = self.page.get_by_role("link", name = "Saree ")

        # Men category locators
        self.men_category = self.page.get_by_role("link", name = "Men")
        self.men_tshirts = self.men_category.get_by_role("link", name = "Tshirts ")
        self.men_jeans = self.men_category.get_by_role("link", name="Jeans ")

        # Kids category locators
        self.kids_category = self.page.locator('a[href="#Kids"][data-toggle="collapse"]')
        self.kids_dress = self.page.get_by_role("link", name="Dress ")
        self.kids_tops = self.page.get_by_role("link", name="Tops & Shirts ")

        # Brand locators
        self.brands = self.page.locator(".brands-name")
        self.polo_brand = self.brands.get_by_role("link", name = "Polo")
        self.hm_brand = self.brands.get_by_role("link", name = "H&M")
        self.madame_brand = self.brands.get_by_role("link", name = "Madame")
        self.mast_harbour_brand = self.brands.get_by_role("link", name = "Mast & Harbour")
        self.babyhug_brand = self.brands.get_by_role("link", name="Babyhug")
        self.allen_solly_junior_brand = self.brands.get_by_role("link", name = "Allen Solly Junior")
        self.kookie_kids_brand = self.brands.get_by_role("link", name = "Kookie Kids")
        self.biba_brand = self.brands.get_by_role("link", name = "Biba")

    def women_category_dress(self):
        """
        Navigate to Women > Dress category.
        """
        self.women_category.click()
        self.women_dress.click()

    def women_category_tops(self):
        """
        Navigate to Women > Tops category.
        """
        self.women_category.click()
        self.women_tops.click()

    def women_category_sarees(self):
        """
        Navigate to Women > Sarees category.
        """
        self.women_category.click()
        self.women_sarees.click()

    def men_category_tshirts(self):
        """
        Navigate to Men > Tshirts category.
        """
        self.men_category.click()
        self.men_tshirts.click()

    def men_category_jeans(self):
        """
        Navigate to Men > Jeans category.
        """
        self.men_category.click()
        self.men_jeans.click()

    def kids_category_dress(self):
        """
        Navigate to Kids > Dress category.
        """
        self.kids_category.click()
        self.kids_dress.click()

    def kids_category_tops(self):
        """
        Navigate to Kids > Tops & Shirts category.
        """
        self.kids_category.click()
        self.kids_tops.wait_for(state="visible")
        self.kids_tops.click()

    def select_polo_brand(self):
        """
        Select Polo brand from brands section.
        """
        self.polo_brand.click()

    def select_hm_brand(self):
        """
        Select H&M brand from brands section.
        """
        self.hm_brand.click()

    def select_madame_brand(self):
        """
        Select Madame brand from brands section.
        """
        self.madame_brand.click()

    def select_mast_harbour_brand(self):
        """
        Select Mast & Harbour brand from brands section.
        """
        self.mast_harbour_brand.click()

    def select_babyhug_brand(self):
        """
        Select Babyhug brand from brands section.
        """
        self.babyhug_brand.click()

    def select_allen_solly_junior_brand(self):
        """
        Select Allen Solly Junior brand from brands section.
        """
        self.allen_solly_junior_brand.click()

    def select_kookie_kids_brand(self):
        """
        Select Kookie Kids brand from brands section.
        """
        self.kookie_kids_brand.click()

    def select_biba_brand(self):
        """
        Select Biba brand from brands section.
        """
        self.biba_brand.click()

