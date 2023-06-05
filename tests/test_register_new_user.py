import time

from handlers.exception_handler import NotEnoughMoneyException
from pages.vipdrive_pages.login_page import LoginPage
from pages.vipdrive_pages.overview_page import OverviewPage
from pages.vipdrive_pages.playlist_page import PlayListPage
from pages.vipdrive_pages.signup_page import SignUpPage
from pages.vipdrive_pages.channel_groups_page import ChannelGroupsPage
from pages.vipdrive_pages.tariff_page import TariffPage
from pages.vipdrive_pages.money_transfer_page import MoneyTransferPage

from pages.ottplayer_pages.signup_page import SignUpPage as OttSignUpPage
from pages.ottplayer_pages.login_page import LoginPage as OttLoginPage
from pages.ottplayer_pages.playlist_page import PlaylistPage as OttPlayListPage


def test_full_registration_flow(browser_driver, data):
    # Create new user
    signup_page = SignUpPage(browser_driver)
    new_user = signup_page.register_new_user()

    # Login as administrator
    login_page = LoginPage(browser_driver)
    login_page.login(email=data.admin_email, password=data.admin_password)

    # Transfer money to the new user
    money_transfer_page = MoneyTransferPage(browser_driver)
    money_transfer_page.transfer_money_to_the_user(email=data.user_email, amount=data.amount)

    # Check balance
    overview_page = OverviewPage(browser_driver)
    overview_page.check_balance()

    money_transfer_page.logout()

    # Login as new user
    login_page = LoginPage(browser_driver)
    login_page.login(data.user_email, password=data.user_password)

    # Config new user's channel group
    channel_group_page = ChannelGroupsPage(browser_driver)
    channel_group_page.config_playlist()

    # Activate tariff
    tariff_page = TariffPage(browser_driver)
    tariff_page.activate_tariff()

    # Get playlist link and logout
    playlist_page = PlayListPage(browser_driver)
    playlist_page.download_playlist()

    # Create new user OTT
    signup_page = OttSignUpPage(browser_driver)
    signup_page.register_new_user(new_user)

    # Login as new user OTT
    login_page = OttLoginPage(browser_driver)
    login_page.login(email=data.user_email, password=data.user_password)

    # Add playlist OTT and go to Settings page
    playlist_page = OttPlayListPage(browser_driver)
    playlist_page.upload_playlist()
    playlist_page.delete_playlist_file()
