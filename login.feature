Feature: Test the login page

  Background:
    Given I am on the login page
    Then I should not see the cart and messages icons

  Scenario: Login with valid credentials
    When I login as user "kangurooscar@gmail.com" and password "admin1234567$"
    Then I should see the cart and messages icons

  Scenario: Login with invalid username
    When I login as user "invalid@gmail.com" and password "admin1234567$"
    Then I should not see the cart and messages icons
    And I should not see the cart and messages icons

  Scenario: Login with invalid password
    When I login as user "kangurooscar@gmail.com" and password "invalid"
    Then I should see login invalid credentials error
    And I should not see the cart and messages icons
