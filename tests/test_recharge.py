import time

from pages.vipdrive_pages.login_page import LoginPage
from pages.vipdrive_pages.money_transfer_page import MoneyTransferPage


def test_recharge(browser_driver):
    # Login as administrator
    login_page = LoginPage(browser_driver)
    time.sleep(5)
    login_page.login_as_admin()

    # Transfer money to the user
    money_transfer_page = MoneyTransferPage(browser_driver)
    with open("temp_files/email_user.txt", "r") as file:
        email = file.readline()
    money_transfer_page.transfer_money_to_the_user(email)

