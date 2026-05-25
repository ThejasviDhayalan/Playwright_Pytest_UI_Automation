# Feature File: Newsletter Subscription
# Description: This feature file defines the test scenarios for newsletter subscription functionality on the automation exercise website.
# Author: Thejasvi Dhayalan
# Date: May 2026

Feature: Newsletter Subscription
  As a registered user
  I want to subscribe to the newsletter
  So that I can receive updates and promotions

  Scenario Outline: User Successfully subscribes to newsletter with valid credentials
    Given the user logs in with valid credentials using "<email>" and "<password>" and "<name>"
    When the user navigates to newsletter subscription section
    When subscribes to newsletter with their email address
    Then the newsletter subscription should be successful
    Then the success confirmation message should be displayed
    Then the user logs out of the application

    Examples: Valid User Credentials
      | email              | password  | name    |
      | userone@gmail.com  | pwd@123   | UserOne |
      | usertwo@gmail.com  | pwd@123   | UserTwo |
