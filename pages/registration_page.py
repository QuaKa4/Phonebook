from selenium.webdriver.common.by import By

from helpers.waiter import Wait
from pages.base_page import BasePage


class RegistrationPageLocators:
    email_input = (By.XPATH, '//*[@id="registration-form"]/div[1]//input')
    password_input = (By.XPATH, '//*[@id="registration-form"]/div[2]//input')
    password_confirm_input = (By.XPATH, '//*[@id="registration-form"]/div[3]//input')
    reg_button = (By.XPATH, '//button[text()=" Sign up "]')
    error_message_create = (By.XPATH, '//*[@id="error-message"]')
    error_message_conf_password = (By.XPATH, '//*[@id="confirm-password-error-matcher"]')
    error_message_password = (By.XPATH, '//*[@id="password-error-minlength"]')
    error_message_email = (By.XPATH, '//*[@id="email-error-invalid"]')
    get_login_link = (By.XPATH, '//*[@id="error-message"]/a')
    disabled_button = (By.XPATH, '//*[@id="registration-form"]/div[4]/div[1]/button[@disabled="true"]')


class RegistrationPage(BasePage):
    url = '/user/registration'

    def _elements_to_wait(self):
        Wait.for_visibility(self.driver, *RegistrationPageLocators.error_message_create)

    def password_input(self, password):
        password_input = self.driver.find_element(*RegistrationPageLocators.password_input)
        password_input.send_keys(password)

    def password_confirm_input(self, password):
        password_confirm_input = self.driver.find_element(*RegistrationPageLocators.password_confirm_input)
        password_confirm_input.send_keys(password)

    def email_input(self, email):
        email_input = self.driver.find_element(*RegistrationPageLocators.email_input)
        email_input.send_keys(email)

    def registration_button_press(self):
        reg_button = self.driver.find_element(*RegistrationPageLocators.reg_button)
        reg_button.click()

    def get_login_link(self):
        link = self.driver.find_element(*RegistrationPageLocators.get_login_link)
        link.click()

    def disabled_button_check(self):
        try:
            self.driver.find_element(*RegistrationPageLocators.disabled_button)
        except:
            print('user can not registrate with wrong data')
