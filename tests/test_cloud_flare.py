from pages.ottplayer_pages.signup_page import SignUpPage as OttSignUpPage
from pages.ottplayer_pages.login_page import LoginPage as OttLoginPage
from pages.ottplayer_pages.playlist_page import PlaylistPage as OttPlayListPage


def test_cloud_flare_killer(browser_driver):
# Create new user OTT
    signup_page = OttSignUpPage(browser_driver)
    signup_page.fill_test_data(username="Arthur", email="sex@gmail.com", password="123456")

    # Login as new user OTT
    # login_page = OttLoginPage(browser_driver)
    # login_page.login_as_user(new_user)
    #
    # # Add playlist OTT and go to Settings page
    # playlist_page = OttPlayListPage(browser_driver)
    # playlist_page.upload_playlist()
    # playlist_page.delete_playlist_file()