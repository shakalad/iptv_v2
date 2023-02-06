import time

from selenium.webdriver import Keys

from pages.base_page import BasePage


class SettingsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    locators = {
        'autoupdate_on': ('xpath', "*//label[@for='autoupdateOn']"),
        'select': ('xpath', "*//div[@class='uk-form-custom']"),
        'ss': ('css', "select"),
        'save_btn': ('xpath', "//*[@id='playlistSet']//button[@type='submit']"),
        'body': ('css', "body")
    }

    def activate_autoupdate(self):
        self.autoupdate_on.click()
        self.select.click()
        self.ss.select_element_by_index(1)
        self.save_btn.click_button()
