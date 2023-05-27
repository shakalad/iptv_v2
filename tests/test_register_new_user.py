import time

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
from pages.ottplayer_pages.settings_page import SettingsPage


def test_full_registration_flow(browser_driver):

    # Create new user
    signup_page = SignUpPage(browser_driver)
    new_user = signup_page.register_new_user()
    with open("temp_files/new_user.txt", "w") as file:
        file.writelines([new_user.email + "\n", new_user.password])

    # Login as administrator
    # login_page = LoginPage(browser_driver)
    # login_page.login_as_admin()
    #
    # # Transfer money to the new user
    # money_transfer_page = MoneyTransferPage(browser_driver)
    # money_transfer_page.transfer_money_to_the_user(new_user.email)
    #
    # # Check balance
    # overview_page = OverviewPage(browser_driver)
    # overview_page.check_balance()
    # money_transfer_page.logout()

    # Login as new user
    login_page = LoginPage(browser_driver)
    login_page.login_as_user(new_user)

    # Config new user's channel group
    channel_group_page = ChannelGroupsPage(browser_driver)
    channel_group_page.config_playlist()

    # Activate tariff
    # tariff_page = TariffPage(browser_driver)
    # tariff_page.activate_tariff(auto_renewal=True)
    # time.sleep(5)

    # Get playlist link and logout
    playlist_page = PlayListPage(browser_driver)
    playlist_link = playlist_page.download_playlist()
    playlist_page.logout()
    print(playlist_link)

    # Create new user OTT
    signup_page = OttSignUpPage(browser_driver)
    signup_page.register_new_user(new_user)

    # Login as new user OTT
    login_page = OttLoginPage(browser_driver)
    login_page.login_as_user(new_user)

    # Add playlist OTT and go to Settings page
    playlist_page = OttPlayListPage(browser_driver)
    playlist_page.upload_playlist()
