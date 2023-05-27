from handlers.json_handler import JsonHandler
from pages.base_page import BasePage


class OverviewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://vipdrive.net/finance/overview"
        self.open(self.url)

    locators = {
        "balance": ('xpath', "*//span[@class='uk-text-lead']"),
    }

    def check_balance(self):
        json_handler = JsonHandler()
        json_handler.update_data('admin_balance', self.balance.get_text())
