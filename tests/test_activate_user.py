import time

from pages.vipdrive_pages.login_page import LoginPage
from pages.vipdrive_pages.money_transfer_page import MoneyTransferPage
from pages.vipdrive_pages.overview_page import OverviewPage
from pages.vipdrive_pages.tariff_page import TariffPage

from handlers.json_handler import JsonHandler


def test_activate(browser_driver):
    json_handler = JsonHandler()

    # Login as administrator
    login_page = LoginPage(browser_driver)
    time.sleep(5)

    # Login as user
    email = json_handler.read_file()['email']
    login_page.login_as_user(email)

    # Activate tariff
    tariff_page = TariffPage(browser_driver)
    tariff_page.activate_tariff()
