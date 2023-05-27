from pages.base_page import BasePage


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

    def activate_tariff(self, auto_renewal):
        while True:
            try:
                self.activation_btn.click_button()
                if auto_renewal:
                    self.auto_renewal_btn.click_button()
                    break
            except Exception as cant_activate:
                print(cant_activate)
