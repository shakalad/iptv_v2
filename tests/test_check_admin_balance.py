from pages.vipdrive_pages.login_page import LoginPage
from pages.vipdrive_pages.overview_page import OverviewPage
from pages.vipdrive_pages.signup_page import SignUpPage


def test_check_admin_balance(browser_driver):
    # Open register page
    signup_page = SignUpPage(browser_driver)

    # Login as Admin
    login_page = LoginPage(browser_driver)
    login_page.login_as_admin()

    # Check balance
    overview_page = OverviewPage(browser_driver)
    overview_page.check_balance()
