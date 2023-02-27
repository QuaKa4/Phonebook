from attr import dataclass

from pages.common import Emails, Passwords
from pages.registration_page import RegistrationPage


class TestUserCanNotReg:
    @dataclass
    class _TestCaseData:
        emails: Emails
        passwords: Passwords

    @staticmethod
    def user_can_not_register_body(driver, test_case_data: _TestCaseData):
        registration_page = RegistrationPage(driver)
        registration_page.navigate_to_url()
        registration_page.password_input(test_case_data.emails)
        registration_page.password_confirm_input(test_case_data.passwords)
        registration_page.email_input(test_case_data.passwords)
        registration_page.disabled_button_check()

        driver.quit()

    def test_user_cant_reg_with_wrong_email(self, driver):
        test_case_data = self._TestCaseData(emails=Emails.WRONG_EMAIL, passwords=Passwords.PASSWORD)
        self.user_can_not_register_body(driver, test_case_data)

    def test_user_cant_reg_with_wrong_password(self, driver):
        test_case_data = self._TestCaseData(emails=Emails.WRONG_EMAIL, passwords=Passwords.WRONG_PASSWORD)
        self.user_can_not_register_body(driver, test_case_data)

    def test_user_cant_reg_with_wrong_username_and_password(self, driver):
        test_case_data = self._TestCaseData(emails=Emails.WRONG_EMAIL, passwords=Passwords.WRONG_PASSWORD)
        self.user_can_not_register_body(driver, test_case_data)

