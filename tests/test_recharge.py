from pages.vipdrive_pages.login_page import LoginPage
from pages.vipdrive_pages.money_transfer_page import MoneyTransferPage
from pages.vipdrive_pages.overview_page import OverviewPage
from pages.vipdrive_pages.tariff_page import TariffPage


def test_recharge(browser_driver, data):

    # Login as administrator
    login_page = LoginPage(browser_driver)
    login_page.login(email=data.admin_email, password=data.admin_password)

    # Transfer money to the user
    money_transfer_page = MoneyTransferPage(browser_driver)
    money_transfer_page.transfer_money_to_the_user(data.user_email, data.amount)

    # Check admin balance
    overview_page = OverviewPage(browser_driver)
    overview_page.check_balance()
    overview_page.logout()

    # Login as user that must be activated
    login_page.login(email=data.user_email, password=data.user_password)

    # Activate user
    tariff_page = TariffPage(browser_driver)
    tariff_page.activate_tariff()


