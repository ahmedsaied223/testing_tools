# Cucumber Testing Framework for Mobile Browser Trading App

## Overview
This project is a Cucumber testing framework designed to test a mobile browser trading application. It utilizes Cucumber for behavior-driven development (BDD) and Ruby for step definitions.

## Project Structure
The project is organized as follows:

```
cucumber-testing-framework
├── features
│   ├── login.feature
│   ├── trade.feature
│   └── step_definitions
│       ├── login_steps.rb
│       └── trade_steps.rb
├── support
│   ├── env.rb
│   └── hooks.rb
├── Gemfile
├── Gemfile.lock
└── README.md
```

## Features
- **Login Feature**: 
  - Located in `features/login.feature`
  - Describes scenarios for user login functionality.

- **Trade Feature**: 
  - Located in `features/trade.feature`
  - Outlines scenarios for executing trades within the app.

## Step Definitions
- **Login Steps**: 
  - Implemented in `features/step_definitions/login_steps.rb`
  - Contains methods corresponding to the steps in the login feature.

- **Trade Steps**: 
  - Implemented in `features/step_definitions/trade_steps.rb`
  - Contains methods corresponding to the steps in the trade feature.

## Support Files
- **Environment Setup**: 
  - `support/env.rb` sets up the necessary environment for running Cucumber tests.

- **Hooks**: 
  - `support/hooks.rb` contains hooks that manage the test lifecycle events.

## Dependencies
The project uses Bundler to manage dependencies. The required gems are specified in the `Gemfile`.

## Getting Started
1. Clone the repository.
2. Navigate to the project directory.
3. Run `bundle install` to install the necessary gems.
4. Execute the tests using `cucumber`.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.