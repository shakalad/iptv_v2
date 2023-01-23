import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from fake_useragent import FakeUserAgent


@pytest.fixture()
def browser_driver():
    driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--window-size=1920,1080')
    # driver_options.add_argument(f"user-agent={FakeUserAgent().chrome}")
    # driver_options.add_argument("--no-sandbox")
    # driver_options.headless = True
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=driver_options)
    driver.maximize_window()
    yield driver
    driver.quit()
