from selenium.webdriver.common.by import By

from helpers.waiter import Wait
from pages.base_page import BasePage
from pages.common import Emails, Passwords


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
        username_input = self.driver.find_element(*LoginPageLocators.email_input)
        username_input.send_keys(username)

    def set_password(self, password):
        password_input = self.driver.find_element(*LoginPageLocators.password_input)
        password_input.send_keys(password)

    def login_button_press(self):
        login_button = self.driver.find_element(*LoginPageLocators.login_button)
        login_button.click()

    def registration_button_press(self):
        regiter_button = self.driver.find_element(*LoginPageLocators.reg_link)
        regiter_button.click()
