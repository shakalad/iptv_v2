from pages.vipdrive_pages.login_page import LoginPage
from pages.vipdrive_pages.overview_page import OverviewPage


def test_check_admin_balance(browser_driver):
    # Login as Admin
    login_page = LoginPage(browser_driver)
    login_page.login_as_admin()

    # Check balance
    # overview_page = OverviewPage(browser_driver)
    # overview_page.check_balance()
