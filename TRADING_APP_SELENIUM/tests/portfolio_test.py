from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from pages.portfolio_page import PortfolioPage
from utils.browser_setup import setup_browser

class PortfolioTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = setup_browser()
        cls.portfolio_page = PortfolioPage(cls.driver)

    def test_view_portfolio(self):
        self.portfolio_page.navigate_to_portfolio()
        portfolio_value = self.portfolio_page.get_portfolio_value()
        self.assertIsNotNone(portfolio_value, "Portfolio value should not be None")

    def test_stock_positions(self):
        self.portfolio_page.navigate_to_portfolio()
        stock_positions = self.portfolio_page.get_stock_positions()
        self.assertGreater(len(stock_positions), 0, "There should be at least one stock position")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
