Feature: Login Feature

Scenario: Success Login with correct credential
    Given I am on the homepage
    When I click Sign in
    And I fill my credential
    Then I should be logged in


Scenario: Fail Login with wrong email
    Given I am on the homepage
    When I click Sign in
    And I fill wrong email
    Then I should not be logged in
    And I should see the error message