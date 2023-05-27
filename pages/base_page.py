from selenium.common import TimeoutException
from seleniumpagefactory import PageFactory
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def logout(self):
        self.driver.get("https://vipdrive.net/auth/signout")

    def element_is_present(self, locator, timeout=10):
        try:
            return wait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            return False


