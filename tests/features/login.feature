Feature: Login Page

  Background: Open Form Authentication page
    Given I have navigated to the "automationteststore.com" page

  Scenario: Login with valid credentials
    When I click on Login link
    When I enter a username of "jella"
    And I enter a password of "password"
    And I click the Login button
#    Then the user account page opens
