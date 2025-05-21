from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from pages.trading_page import TradingPage
from utils.config import BASE_URL

class TestTrading:

    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        self.trading_page = TradingPage(self.driver)
        yield
        self.driver.quit()

    def test_place_trade(self, setup):
        self.trading_page.place_order("AAPL", 10)
        assert self.trading_page.is_order_successful() == True

    def test_check_balance(self, setup):
        balance = self.trading_page.get_balance()
        assert balance >= 0

    def test_view_market_data(self, setup):
        market_data = self.trading_page.get_market_data("AAPL")
        assert market_data is not None
        assert len(market_data) > 0

    def test_cancel_trade(self, setup):
        self.trading_page.place_order("GOOGL", 5)
        self.trading_page.cancel_order("GOOGL")
        assert self.trading_page.is_order_cancelled("GOOGL") == True