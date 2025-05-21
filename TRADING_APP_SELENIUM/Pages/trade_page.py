class TradePage:
    def __init__(self, driver):
        self.driver = driver
        self.stock_selector = "selector_for_stock"  # Replace with actual selector
        self.quantity_input = "selector_for_quantity"  # Replace with actual selector
        self.submit_button = "selector_for_submit"  # Replace with actual selector

    def select_stock(self, stock_name):
        stock_element = self.driver.find_element_by_css_selector(self.stock_selector)
        stock_element.click()
        stock_element.send_keys(stock_name)

    def enter_quantity(self, quantity):
        quantity_element = self.driver.find_element_by_css_selector(self.quantity_input)
        quantity_element.clear()
        quantity_element.send_keys(quantity)

    def submit_trade(self):
        submit_element = self.driver.find_element_by_css_selector(self.submit_button)
        submit_element.click()
      
