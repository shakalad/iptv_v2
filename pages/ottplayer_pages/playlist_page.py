import time

from pages.base_page import BasePage


class PlaylistPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://ottplayer.tv/playlist/original"
        self.open(self.url)

    locators = {
        'playlist_name': ('CSS', "input[name='name']"),
        'playlist_link_toggle': ('CSS', "div#sources_toggle:nth-child(2)"),
        'playlist_link': ('CSS', "input[name='source']"),
        'playlist_upload_input': ('XPATH', "*//input[@id='inplaylist']"),
        'submit_btn': ('CSS', "button[type='submit']"),
        'settings_btn': ('XPATH', "*//a[@uk-icon='settings']")
    }


def add_playlist(self, playlist_link):
    # TODO: update a method to upload playlist file
    while self.driver.current_url == self.url:
        self.driver.refresh()
        time.sleep(10)
        self.playlist_name.set_text("IPTV")
        self.playlist_link_toggle.click_button()
        self.playlist_link.set_text(playlist_link)
        self.submit_btn.click_button()


def upload_playlist(self):
    self.playlist_name.set_text("IPTV")
    self.playlist_link_toggle.click_button()
    self.playlist_link.playlist_upload_input.send_keys('playlist.m3u8')
    self.submit_btn.click_button()
