from pages.base_page import BasePage


class PlayListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://vipdrive.net/playlist/download"
        self.open(self.url)

    locators = {
        'playlist_link': ('CSS', "div[id='pllink2']"),
        'playlist_download': ('XPATH', "*//button[@id='setFileType']")
    }

    def download_playlist(self):
        self.playlist_download.click()
        playlist_link: str = self.playlist_link.get_text()
        self._json_handler.update_data("playlist_link", playlist_link)
