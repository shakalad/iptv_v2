import base64

import pytest
import pytest_html

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser_driver():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--window-size=1920,1080')
    driver_options.add_argument("--no-sandbox")
    driver_options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=driver_options)
    driver.maximize_window()
    yield driver
    driver.quit()
