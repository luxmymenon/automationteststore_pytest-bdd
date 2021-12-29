# Created by luxmy at 2021-12-28
Feature: Home page tests
  # Enter feature description here

  Background: Access home page
    Given I have navigated to the "automationteststore.com" page

  Scenario: Click on account link and then login link
    When I click on Accounts link
    When I click on Login link


#    Then the user account page opens