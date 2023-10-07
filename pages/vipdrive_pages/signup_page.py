import time


from email_module.vipdrive_verification_module import get_vipdrive_registration_verification_code
from generator.generator import generated_user
from pages.base_page import BasePage


class SignUpPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://vipdrive.net/welcome/signup/e804c47574f73528"
        self.open(self.url)

    locators = {
        'username': ('CSS', "input[name='username']"),
        'email': ('CSS', "input[name='email']"),
        'password': ('CSS', "input[name='password']"),
        're_password': ('CSS', "input[name='repassword']"),
        'verification_code': ('CSS', "input[name='code']"),
        'submit_btn': ('CSS', "button[type='submit']"),
    }

    def register_new_user(self):
        # registration
        user = next(generated_user())
        self.username.set_text(user.username)
        self.email.set_text(user.email)
        self.password.set_text(user.password)
        self.re_password.set_text(user.repassword)
        self.submit_btn.click()

        # verification
        self.email.set_text(user.email)
        time.sleep(10)
        verification_code = get_vipdrive_registration_verification_code()
        self.verification_code.set_text(verification_code)
        self.submit_btn.click()

        print(f"Email: {user.email}\n"
              f"Password: {user.password}\n"
              f"Username: {user.username}\n"
              f"Verification Code: {verification_code}")

        return user
