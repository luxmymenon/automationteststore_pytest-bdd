# Created by luxmy at 2021-12-28
Feature: Add featured product to cart
  # Enter feature description here

  Background: Access home page
    Given I have navigated to the "automationteststore.com" page

  Scenario: Scroll to featured product list
    When I click on the add to cart thumbnail of the first featured product
    When I click Cart thumbnail
    When I click on Checkout button
    Then I am directed to login page
