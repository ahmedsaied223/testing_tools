class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def wait_for_element(self, by, value, timeout=10):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        element = self.driver.find_element(by, value)
        element.click()

    def enter_text(self, by, value, text):
        element = self.driver.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, by, value):
        element = self.driver.find_element(by, value)
        return element.text

    def is_element_visible(self, by, value):
        from selenium.common.exceptions import NoSuchElementException
        try:
            self.driver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False