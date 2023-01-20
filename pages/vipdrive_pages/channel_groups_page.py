from pages.base_page import BasePage


class ChannelGroupsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://vipdrive.net/playlist/groups"
        self.open(self.url)

    locators = {
        'adults_chk': ('CSS', "input[value='10']"),
        'armenian_chk': ('CSS', "input[value='11']"),
        'ukrainian_chk': ('CSS', "input[value='12']"),
        'usa_chk': ('CSS', "input[value='13']"),
        'belorus_chk': ('CSS', "input[value='15']"),
        'azer_chk': ('CSS', "input[value='16']"),
        'kazakh_chk': ('CSS', "input[value='18']"),
        'tochik_chk': ('CSS', "input[value='19']"),
        'uzbek_chk': ('CSS', "input[value='20']"),
        'moldova_chk': ('CSS', "input[value='21']"),
        'turkish_chk': ('CSS', "input[value='22']"),
        'greece_chk': ('CSS', "input[value='23']"),
        'submit_btn': ('CSS', "button[type='submit']")
    }

    def config_playlist(self):
        self.adults_chk.click_button()
        self.armenian_chk.click_button()
        self.ukrainian_chk.click_button()
        self.usa_chk.click_button()
        self.belorus_chk.click_button()
        self.azer_chk.click_button()
        self.kazakh_chk.click_button()
        self.tochik_chk.click_button()
        self.uzbek_chk.click_button()
        self.moldova_chk.click_button()
        self.turkish_chk.click_button()
        self.greece_chk.click_button()
        self.submit_btn.click_button()
