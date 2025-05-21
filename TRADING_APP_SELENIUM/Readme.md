# Trading Application Selenium WebDriver

This project is a Selenium WebDriver workspace for a trading application. It includes automated tests for various functionalities of the application, ensuring that the trading processes work as expected.

## Project Structure

```
trading-app-selenium
├── src
│   ├── tests
│   │   ├── login_test.py          # Test cases for login functionality
│   │   ├── trade_execution_test.py # Test cases for executing trades
│   │   └── portfolio_test.py       # Test cases for portfolio management
│   ├── pages
│   │   ├── login_page.py           # Page object for login page
│   │   ├── trade_page.py           # Page object for trade page
│   │   └── portfolio_page.py       # Page object for portfolio page
│   └── utils
│       ├── browser_setup.py        # Browser setup and teardown functions
│       └── helpers.py              # Utility functions for tests
├── requirements.txt                 # Project dependencies
├── .gitignore                       # Files and directories to ignore by Git
└── README.md                        # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd trading-app-selenium
   ```

2. **Install dependencies**:
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the tests**:
   You can run the tests using a test runner like pytest:
   ```
   pytest src/tests
   ```

## Usage

- The tests are organized into separate files based on functionality.
- Each test file imports the relevant page classes and utilizes Selenium WebDriver to perform actions and assertions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
