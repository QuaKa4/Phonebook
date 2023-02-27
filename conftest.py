import chromedriver_autoinstaller
import pytest as pytest
from selenium import webdriver


@pytest.fixture
def driver():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.set_window_position(0, 0)
    driver.implicitly_wait(5)
    return driver
