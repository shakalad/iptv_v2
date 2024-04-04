import time

from handlers.user_handler import User
from pages.vipdrive_pages.login_page import LoginPage
from pages.vipdrive_pages.money_transfer_page import MoneyTransferPage
from pages.vipdrive_pages.overview_page import OverviewPage
from pages.vipdrive_pages.tariff_page import TariffPage

from handlers.json_handler import JsonHandler


def test_recharge(browser_driver):
    json_handler = JsonHandler()

    # Login as administrator
    login_page = LoginPage(browser_driver)
    time.sleep(5)
    login_page.login_as_admin()

    # Transfer money to the user
    money_transfer_page = MoneyTransferPage(browser_driver)
    email = json_handler.read_file()['email']
    amount = json_handler.read_file()['amount']
    money_transfer_page.transfer_money_to_the_user(email, amount)

    # Check admin balance
    overview_page = OverviewPage(browser_driver)
    overview_page.check_balance()

    # Logout from admin
    login_page.logout()

    # Login as user
    login_page.login_as_user(email)

    # Activate tariff
    tariff_page = TariffPage(browser_driver)
    tariff_page.activate_tariff()

    # Logout from admin
    money_transfer_page.logout()

    # Login as user
    user_credentials = User(email=email, password="904070")
    login_page = LoginPage(browser_driver)
    login_page.login_as_user(user_credentials)

    # Activate tariff
    tariff_page = TariffPage(browser_driver)
    tariff_page.activate_tariff()
