Given("I am on the trading page") do
  visit '/trading'
end

When("I place a trade for {string} shares of {string}") do |quantity, stock|
  fill_in 'Quantity', with: quantity
  fill_in 'Stock', with: stock
  click_button 'Place Trade'
end

Then("I should see a confirmation message for my trade") do
  expect(page).to have_content('Trade placed successfully')
end

Then("I should see my trade in the trade history") do
  visit '/trade_history'
  expect(page).to have_content('Your Trades')
end

Given("the user is logged in") do
  visit '/login'
  fill_in 'Username', with: 'test_user'
  fill_in 'Password', with: 'password123'
  click_button 'Login'
  expect(page).to have_content('Welcome, test_user')
end

When("the user selects a stock to trade") do
  visit '/trading'
  fill_in 'Stock', with: 'AAPL'
end

When("the user enters a quantity that exceeds available funds") do
  fill_in 'Quantity', with: '10000' # Example quantity exceeding funds
end

When("the user confirms the trade") do
  click_button 'Place Trade'
end

Then("the trade should not be executed") do
  expect(page).not_to have_content('Trade placed successfully')
end

Then("the user should see an error message indicating insufficient funds") do
  expect(page).to have_content('Error: Insufficient funds')
end

When("the user selects an invalid stock to trade") do
  fill_in 'Stock', with: 'INVALID_STOCK'
end

Then("the user should see an error message indicating invalid stock selection") do
  expect(page).to have_content('Error: Invalid stock selection')
end

When("the trade API times out") do
  # Simulate API timeout (mock or stub the API response)
  allow_any_instance_of(TradeAPI).to receive(:execute_trade).and_raise(Timeout::Error)
end

Then("the user should see an error message indicating a timeout occurred") do
  expect(page).to have_content('Error: Trade request timed out')
end

When("the trade API returns an invalid response") do
  # Simulate invalid API response (mock or stub the API response)
  allow_any_instance_of(TradeAPI).to receive(:execute_trade).and_return(nil)
end

Then("the user should see an error message indicating a system error") do
  expect(page).to have_content('Error: System error occurred')
end

Given("the user is not logged in") do
  visit '/logout' # Ensure the user is logged out
end

When("the user attempts to execute a trade") do
  visit '/trading'
  fill_in 'Stock', with: 'AAPL'
  fill_in 'Quantity', with: '10'
  click_button 'Place Trade'
end

Then("the user should see an error message indicating unauthorized access") do
  expect(page).to have_content('Error: Unauthorized access')
end