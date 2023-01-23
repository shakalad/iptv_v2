import time

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://vipdrive.net/auth/login"
        self.open(self.url)

    locators = {
        'email': ('CSS', "input[name='email']"),
        'password': ('CSS', "input[name='password']"),
        'submit_btn': ('CSS', "button[type='submit']")
    }

    def login_as_admin(self):
        time.sleep(10)
        self.email.set_text("shakalad92@gmail.com")
        self.password.set_text("otxqfw2u")
        self.submit_btn.click_button()

    def login_as_user(self, user):
        time.sleep(5)
        self.email.set_text(user.email)
        self.password.set_text(user.password)
        self.submit_btn.click_button()
