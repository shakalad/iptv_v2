import time

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://ottplayer.tv/account/login"
        self.open(self.url)

    locators = {
        'email': ('CSS', "input[name='email']"),
        'password': ('CSS', "input[name='password']"),
        'submit_btn': ('CSS', "button[type='submit']"),
    }

    def login(self, email, password):
        time.sleep(5)
        self.email.set_text(email)
        self.password.set_text(password)
        self.submit_btn.click_button()
