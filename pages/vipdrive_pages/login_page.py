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
            self.password.set_text("otxqfsw2u")
            self.submit_btn.click_button()
            time.sleep(5)
            self.driver.switch_to.frame(self.iframe.get_web_element())
            print("###############^^^^^^^%%%%%%%%%%%%%%%%%%")
            self.captcha_textarea.setAttribute("display", "initial")
            # self.driver.execute_script(
            #     f"document.getElementById('g-recaptcha-response').style.display = 'initial';")
            self.driver.execute_script(
                f"document.getElementById('g-recaptcha-response').innerHTML='{'sexyyyyyyyyyyyyyy'}';")
            time.sleep(40)

        # if self.driver.current_url == self.url:
        #     print("SEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        #     self.email.set_text("shakalad92@gmail.com")
        #     self.password.set_text("otxqfw2u")
        #     self.driver.execute_script(f"document.getElementById('g-recaptcha-response').setAttribute('display', "
        #                                f"'block');")
        #     time.sleep(1000)
        # self.driver.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML='{solve_captcha()}';")
        #     self.submit_btn.click_button()

    def login_as_user(self, user):
        time.sleep(5)
        self.email.set_text(user.email)
        self.password.set_text(user.password)
        self.submit_btn.click_button()
