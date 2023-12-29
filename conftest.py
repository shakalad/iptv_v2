import pytest
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture()
def browser_driver():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--window-size=1920,1080')
    driver_options.add_argument("--no-sandbox")
    # driver_options.add_argument('--headless')
    driver_options.add_argument("--disable-gpu")
    driver_options.add_experimental_option('prefs', {
        'download.default_directory': os.path.join(os.getcwd(), 'temp_files'),
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True
    })

    driver_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver_options.add_experimental_option("useAutomationExtension", False)
    driver_options.add_argument("--disable-blink-features=AutomationControlled")
    driver_options.add_argument("--disable-extensions")
    driver_options.add_argument("--disable-infobars")
    driver_options.add_argument("--disable-dev-shm-usage")
    driver_options.add_argument("--disable-browser-side-navigation")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=driver_options)
    yield driver
    driver.quit()
