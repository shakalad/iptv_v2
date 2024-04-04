import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec

from handlers.json_handler import JsonHandler


class BasePage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self._json_handler = JsonHandler

    def open(self, url):
        self.driver.get(url)

    def logout(self):
        self.driver.get("https://vipdrive.net/auth/signout")

    def element_is_present(self, locator, timeout=10):
        try:
            return wait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            return False

    def bypass_cloud_flare(self, url: str) -> None:
        self.driver.execute_script(f"window.open('{url}', '_blank')")
        time.sleep(15)
        self.driver.switch_to.window(self.driver.window_handles[1])
