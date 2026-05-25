# Feature File: Order Placement
# Description: This feature file defines the test scenarios for order placement functionality on the automation exercise website.
# Author: Thejasvi Dhayalan
# Date: May 2026

Feature: Order Placement
  As a registered user
  I want to place an order with valid credentials
  So that I can purchase products successfully

  Scenario: User Successfully place an order with valid credentials
    Given the user logs in with valid credentials
    When the user selects products
    Then the cart should contain the selected products
    And the product count should match
    And the product names should match
    And the user proceeds to checkout
    Then the total price should be verified
    When the user places the order
    And the user enters valid payment details
    Then the order should be placed successfully
    And the user logs out of the application
