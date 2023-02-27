from pages.common import Emails, Passwords
from pages.registration_page import RegistrationPage


def test_user_can_register(driver):
    registration_page = RegistrationPage(driver)
    registration_page.navigate_to_url()
    registration_page.password_input(Emails.EMAIL)
    registration_page.password_confirm_input(Passwords.PASSWORD)
    registration_page.email_input(Passwords.PASSWORD)
    registration_page.registration_button_press()
    registration_page.wait_for_load()
    driver.quit()
