require 'cucumber'

Before do
  # Code to run before each scenario
end

After do |scenario|
  if scenario.failed?
    # Code to run if the scenario fails
  end
end