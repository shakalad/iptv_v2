import time

from selenium.webdriver.common.by import By

from email_module.transaction_verification_module import get_transaction_verification_code
from pages.base_page import BasePage
from handlers.exception_handler import NotEnoughMoneyException


class MoneyTransferPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://vipdrive.net/finance/moneytransfer"
        self.open(self.url)

    locators = {
        "recipient_email": ('CSS', "input[name='email']"),
        "trans_amount": ('CSS', "input[id='mTransAmount']"),
        "confirmation_method": ('CSS', "select[name='code_transport']"),
        "trans_submit_btn": ('CSS', "button[id='mTransBtn']"),
        "verification_code": ('CSS', "input[name='code']"),
        "submit_btn": ('CSS', "button[type='submit']"),
    }

    def transfer_money_to_the_user(self, email, amount="1"):
        self.recipient_email.set_text(email)
        self.trans_amount.clear_text()
        self.trans_amount.set_text(amount)
        self.confirmation_method.select_element_by_value("email")
        self.element_is_present((By.CSS_SELECTOR, "button[id='mTransBtn']")).submit()

        # Check for enough money
        # if self.element_is_present((By.XPATH, "*//div[@class='uk-notification-message uk-notification-message-warning']")):
        #     raise NotEnoughMoneyException

        self.verification_code.set_text(get_transaction_verification_code())
        self.submit_btn.click_button()
        time.sleep(5)
