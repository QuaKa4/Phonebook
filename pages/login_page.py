from selenium.webdriver.common.by import By

from helpers.waiter import Wait
from pages.base_page import BasePage
from pages.common import Emails, Passwords
# Extra import, you need to remove


class LoginPageLocators:
    email_input = (By.XPATH, '//div[@class="row"][1]//input')
    password_input = (By.XPATH, '//div[@class="row"][2]//input')
    login_button = (By.XPATH, '//*[@class="btn btn-info my-1 btn-block"]')
    reg_link = (By.XPATH, '//*[text()="Register new Account"]')


class LoginPage(BasePage):
    url = 'user/login'

    def _elements_to_wait(self):
        Wait.for_visibility(self.driver, *LoginPageLocators.reg_link)

    def set_email(self, username):
        self.driver.find_element(*LoginPageLocators.email_input).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*LoginPageLocators.password_input).send_keys(password)

    # click_on_login_button
    def login_button_press(self):
        self.driver.find_element(*LoginPageLocators.login_button).click()

    # click_on_registration_link
    def registration_button_press(self):
        self.driver.find_element(*LoginPageLocators.reg_link).click()
