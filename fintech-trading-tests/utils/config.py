# utils/config.py

class Config:
    BASE_URL = "https://your-fintech-trading-app.com"
    LOGIN_URL = f"{BASE_URL}/login"
    TRADING_URL = f"{BASE_URL}/trading"
    TIMEOUT = 10
    RETRY_COUNT = 3
    HEADLESS = True  # Set to False if you want to see the browser during tests

    @staticmethod
    def get_browser_options():
        from selenium.webdriver.chrome.options import Options
        options = Options()
        if Config.HEADLESS:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        return options