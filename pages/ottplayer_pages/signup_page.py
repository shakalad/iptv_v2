import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from email_module.ottplayer_verification_module import get_ottplayer_registration_activation_link


class SignUpPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://ottplayer.tv/account/registration"
        self.bypass_cloud_flare(url=self.url)

    locators = {
        'username': ('XPATH', "*//input[@name='username']"),
        'email': ('CSS', "input[name='email']"),
        'password': ('CSS', "input[name='password']"),
        're_password': ('CSS', "input[name='repassword']"),
        'verification_code': ('CSS', "input[name='code']"),
        'submit_btn': ('CSS', "button[type='submit']"),
    }

    def register_new_user(self, user):
        # registration
        self.username.set_text(user.username)
        self.email.set_text(user.email)
        self.password.set_text(user.password)
        self.re_password.set_text(user.repassword)
        self.submit_btn.click()

        # activation
        time.sleep(10)
        self.open(get_ottplayer_registration_activation_link())

    def fill_test_data(self, username: str, email: str, password: str) -> None:
        self.username.set_text(username)
        self.email.set_text(email)
        self.password.set_text(password)
