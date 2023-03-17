from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.common import Emails, Passwords


def login_test_helper(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_url()
    login_page.set_email(Emails.EMAIL)
    login_page.set_password(Passwords.PASSWORD)
    login_page.click_on_login_button()
    main_page = MainPage(driver)
    main_page.wait_for_load()


