from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from pages.trade_page import TradePage
from utils.browser_setup import setup_browser

class TradeExecutionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = setup_browser()
        cls.trade_page = TradePage(cls.driver)

    def test_execute_trade(self):
        """Test successful trade execution."""
        self.trade_page.select_stock("AAPL")
        self.trade_page.enter_quantity(10)
        result = self.trade_page.submit_trade()
        self.assertTrue(result, "Trade execution failed.")

    def test_execute_trade_with_invalid_stock(self):
        """Test trade execution with an invalid stock symbol."""
        self.trade_page.select_stock("INVALID")
        self.trade_page.enter_quantity(10)
        result = self.trade_page.submit_trade()
        self.assertFalse(result, "Trade executed with an invalid stock symbol.")

    def test_execute_trade_with_zero_quantity(self):
        """Test trade execution with zero quantity."""
        self.trade_page.select_stock("AAPL")
        self.trade_page.enter_quantity(0)
        result = self.trade_page.submit_trade()
        self.assertFalse(result, "Trade executed with zero quantity.")

    def test_execute_trade_with_negative_quantity(self):
        """Test trade execution with negative quantity."""
        self.trade_page.select_stock("AAPL")
        self.trade_page.enter_quantity(-5)
        result = self.trade_page.submit_trade()
        self.assertFalse(result, "Trade executed with negative quantity.")

    def test_execute_trade_without_selecting_stock(self):
        """Test trade execution without selecting a stock."""
        self.trade_page.enter_quantity(10)
        result = self.trade_page.submit_trade()
        self.assertFalse(result, "Trade executed without selecting a stock.")

    def test_execute_trade_with_large_quantity(self):
        """Test trade execution with a very large quantity."""
        self.trade_page.select_stock("AAPL")
        self.trade_page.enter_quantity(1000000)
        result = self.trade_page.submit_trade()
        self.assertTrue(result, "Trade execution failed for a large quantity.")

    def test_execute_trade_with_special_characters_in_stock(self):
        """Test trade execution with special characters in stock symbol."""
        self.trade_page.select_stock("@#$%")
        self.trade_page.enter_quantity(10)
        result = self.trade_page.submit_trade()
        self.assertFalse(result, "Trade executed with special characters in stock symbol.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

