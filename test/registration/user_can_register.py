from pages.common import Emails, Passwords
from pages.registration_page import RegistrationPage


def test_register_new_user(driver):
    registration_page = RegistrationPage(driver)
    registration_page.navigate_to_url()
    registration_page.email_input(Emails.EMAIL_FOR_REGISTRATION)
    registration_page.password_confirm_input(Passwords.PASSWORD)
    registration_page.fill_password_input(Passwords.PASSWORD)
    registration_page.click_on_registration_button()
    registration_page.wait_for_load()
    registration_page.check_successful_registration()
    driver.quit()

