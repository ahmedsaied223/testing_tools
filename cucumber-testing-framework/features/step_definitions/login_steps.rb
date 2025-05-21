Given("I am on the login page") do
  visit '/login'
end

When("I enter my username as {string}") do |username|
  fill_in 'username', with: username
end

When("I enter my password as {string}") do |password|
  fill_in 'password', with: password
end

When("I click the login button") do
  click_button 'Login'
end

Then("I should see the welcome message") do
  expect(page).to have_content('Welcome')
end

Then("I should see an error message") do
  expect(page).to have_content('Invalid credentials')
end