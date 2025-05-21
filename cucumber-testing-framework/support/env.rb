require 'cucumber'
require 'capybara/cucumber'
require 'selenium-webdriver'

Capybara.default_driver = :selenium
Capybara.app_host = 'https://your-trading-app-url.com'

Before do
  # Code to run before each scenario
end

After do
  # Code to run after each scenario
end