Feature: Trading Functionality

  Scenario: Successful trade execution
    Given the user is logged in
    When the user selects a stock to trade
    And the user enters the quantity to trade
    And the user confirms the trade
    Then the trade should be executed successfully
    And the user should see a confirmation message

  Scenario: Insufficient funds for trade
    Given the user is logged in
    When the user selects a stock to trade
    And the user enters a quantity that exceeds available funds
    And the user confirms the trade
    Then the trade should not be executed
    And the user should see an error message indicating insufficient funds

  Scenario: Invalid stock selection
    Given the user is logged in
    When the user selects an invalid stock to trade
    And the user enters a quantity to trade
    And the user confirms the trade
    Then the trade should not be executed
    And the user should see an error message indicating invalid stock selection

  Scenario: Trade API timeout
    Given the user is logged in
    When the user selects a stock to trade
    And the user enters the quantity to trade
    And the trade API times out
    Then the trade should not be executed
    And the user should see an error message indicating a timeout occurred

  Scenario: Trade API invalid response
    Given the user is logged in
    When the user selects a stock to trade
    And the user enters the quantity to trade
    And the trade API returns an invalid response
    Then the trade should not be executed
    And the user should see an error message indicating a system error

  Scenario: Trade API unauthorized access
    Given the user is not logged in
    When the user attempts to execute a trade
    Then the trade should not be executed
    And the user should see an error message indicating unauthorized access  