class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = "input[name='username']"
        self.password_field = "input[name='password']"
        self.login_button = "button[type='submit']"
        self.error_message = ".error-message"

    def enter_username(self, username):
        self.wait_for_element(self.username_field)
        self.driver.find_element_by_css_selector(self.username_field).send_keys(username)

    def enter_password(self, password):
        self.wait_for_element(self.password_field)
        self.driver.find_element_by_css_selector(self.password_field).send_keys(password)

    def click_login(self):
        self.wait_for_element(self.login_button)
        self.driver.find_element_by_css_selector(self.login_button).click()

    def get_error_message(self):
        self.wait_for_element(self.error_message)
        return self.driver.find_element_by_css_selector(self.error_message).text

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()