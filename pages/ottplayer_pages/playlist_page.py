import os
import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


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

    def upload_playlist(self):
        self.playlist_name.set_text("IPTV")
        upload_input = self.element_is_present((By.XPATH, "*//input[@id='inplaylist']"))
        upload_input.send_keys(os.path.join(os.getcwd(), 'temp_files/playlist.m3u8'))
        # self.playlist_link.playlist_upload_input.send_text()
        self.submit_btn.click_button()

    def delete_playlist_file(self):
        os.remove(os.path.join(os.getcwd(), 'temp_files/playlist.m3u8'))
