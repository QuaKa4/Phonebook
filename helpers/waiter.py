from typing import Union

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT = 30


class Wait:

    @staticmethod
    def for_visibility(
            driver_or_element: Union[WebDriver, WebElement],
            locator: Union[str, By],
            locator_value: str,
            message: str = '',
            timeout: int = TIMEOUT,
    ):
        if not message:
            message = f'Timeout to wait element "{locator_value}" visibility'
        try:
            WebDriverWait(driver_or_element, timeout).until(
                ec.visibility_of_element_located((locator, locator_value)), message=message
            )
        except TimeoutException:
            if isinstance(driver_or_element, WebDriver):
                raise TimeoutException(message)