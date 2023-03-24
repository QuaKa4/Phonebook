from dataclasses import dataclass
from pages.common import Passwords
from pages.common import Emails
from pages.login_page import LoginPage


class TestLoginWithWrongData:
    @dataclass
    class _TestCaseData:
        emails: Emails
        password: Passwords

    @staticmethod
    def _test_method(driver, test_case_data: _TestCaseData):
        login_page = LoginPage(driver)
        login_page.navigate_to_url()
        login_page.wait_for_load()
        login_page.set_email(test_case_data.emails)
        login_page.set_password(test_case_data.password)
        login_page.click_on_login_button()
        login_page.wait_for_load()
        driver.quit()

    def test_user_cant_login_with_wrong_username(self, driver):
        test_case_data = self._TestCaseData(emails=Emails.WRONG_EMAIL, password=Passwords.PASSWORD)
        self._test_method(driver, test_case_data)

    def test_user_cant_login_with_wrong_password(self, driver):
        test_case_data = self._TestCaseData(emails=Emails.WRONG_EMAIL, password=Passwords.WRONG_PASSWORD)
        self._test_method(driver, test_case_data)

    def test_user_cant_login_with_wrong_username_and_password(self, driver):
        test_case_data = self._TestCaseData(emails=Emails.WRONG_EMAIL, password=Passwords.WRONG_PASSWORD)
        self._test_method(driver, test_case_data)
