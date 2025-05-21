class PortfolioPage:
    def __init__(self, driver):
        self.driver = driver
        self.portfolio_value_locator = "portfolio_value_selector"  # Replace with actual selector
        self.stock_positions_locator = "stock_positions_selector"  # Replace with actual selector

    def get_portfolio_value(self):
        portfolio_value_element = self.driver.find_element_by_css_selector(self.portfolio_value_locator)
        return portfolio_value_element.text

    def get_stock_positions(self):
        stock_positions_element = self.driver.find_elements_by_css_selector(self.stock_positions_locator)
        return [position.text for position in stock_positions_element]
