from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

class TestLogin:
    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()  # or any other driver you prefer
        self.driver.get("https://your-fintech-trading-app-url.com/login")
        yield
        self.driver.quit()

    def test_successful_login(self, setup):
        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        username_input.send_keys("valid_username")
        password_input.send_keys("valid_password")
        login_button.click()

        time.sleep(2)  # wait for the page to load
        assert "Dashboard" in self.driver.title  # replace with actual title or element check

    def test_unsuccessful_login(self, setup):
        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        username_input.send_keys("invalid_username")
        password_input.send_keys("invalid_password")
        login_button.click()

        time.sleep(2)  # wait for the error message to appear
        error_message = self.driver.find_element(By.XPATH, "//div[@class='error-message']")
        assert error_message.is_displayed()  # replace with actual error message check