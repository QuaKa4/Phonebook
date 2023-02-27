from urllib.parse import urljoin

import pytest
from selenium.common import TimeoutException


class BasePage:
    url: str

    def __init__(self, driver):
        self.driver = driver

    def _elements_to_wait(self):
        pass

    def wait_for_load(self):
        try:
            self._elements_to_wait()
        except TimeoutException as e:
            pytest.fail(e.msg)

    def make_url(self, **kwargs):
        if not hasattr(self, 'url'):
            raise AttributeError(f'Page "{self.__class__.__name__}" does not have "url" attribute, please declare it!')
        return urljoin(base='http://phonebook.telran-edu.de:8080/', url=self.url, allow_fragments=False).format(**kwargs)

    def navigate_to_url(self, **kwargs):
        url = self.make_url(**kwargs)
        self.driver.get(url)
