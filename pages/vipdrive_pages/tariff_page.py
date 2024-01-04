from pages.base_page import BasePage

from selenium.common.exceptions import TimeoutException


class TariffPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://vipdrive.net/tariff/info"
        self.open(self.url)

    locators = {
        'activation_btn': ('CSS', "button[id='actTariffBtn']"),
        'auto_renewal_btn': ('CSS', "button[id='actAutoBtn']"),
    }

    def activate_tariff(self):
        for i in range(3):
            try:
                self.activation_btn.click_button()
                break
            except TimeoutException as cant_activate:
                print(cant_activate)
                break
            except Exception as e:
                print(f"Unexpected error: {e}")
