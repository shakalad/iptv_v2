import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from captcha_module.captcha_solver import solve_captcha


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://vipdrive.net/auth/login"
        self.open(self.url)

    locators = {
        'email': ('CSS', "input[name='email']"),
        'password': ('CSS', "input[name='password']"),
        'submit_btn': ('CSS', "button[type='submit']"),
        'iframe': ('XPATH', "*//iframe[@title='reCAPTCHA']"),
        'modal': ('XPATH', "*//div[@class='uk-notification uk-notification-top-right']"),
        'captcha_textarea': ('XPATH', "*//textarea[@id='g-recaptcha-response']")
    }

    def login_as_admin(self):
        while True:
            self.email.set_text("shakalad92@gmail.com")
            self.password.set_text("otxqfw2u")
            self.submit_btn.click_button()
            if self.element_is_present((By.XPATH, "*//iframe[@title='reCAPTCHA']")):
                self.email.set_text("shakalad92@gmail.com")
                self.password.set_text("otxqfw2u")
                self.driver.execute_script(f"document.getElementById('g-recaptcha-response').style.display='initial';")
                self.driver.execute_script(
                    f"document.getElementById('g-recaptcha-response').innerHTML='{solve_captcha()}';")
                self.submit_btn.click_button()
                print("### SUCCESS YOU ARE LOGED IN AS ADMIN")
                break
            break

    def login_as_user(self, user, password: str = "904070"):
        while True:
            self.email.set_text(user.email)
            self.password.set_text(password)
            self.submit_btn.click_button()
            if self.element_is_present((By.XPATH, "*//iframe[@title='reCAPTCHA']")):
                self.email.set_text(user.email)
                self.password.set_text(password)
                self.driver.execute_script(f"document.getElementById('g-recaptcha-response').style.display='initial';")
                self.driver.execute_script(
                    f"document.getElementById('g-recaptcha-response').innerHTML='{solve_captcha()}';")
                self.submit_btn.click_button()
                print(f"### SUCCESS YOU ARE LOGED IN AS {user.email}")
                break
            break
