import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from handlers.data_handler import DataHandler


@pytest.fixture()
def browser_driver():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--window-size=1920,1080')
    driver_options.add_argument("--no-sandbox")
    driver_options.add_argument('--headless=new')
    driver_options.add_experimental_option('prefs', {
        'download.default_directory': os.path.join(os.getcwd(), 'temp_files'),
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True
    })
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=driver_options)
    # driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def data():
    data = DataHandler()
    yield data
