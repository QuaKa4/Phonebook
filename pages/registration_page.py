from selenium.webdriver.common.by import By

from helpers.waiter import Wait
from pages.base_page import BasePage


class RegistrationPageLocators:
    email_input = (By.XPATH, '//*[@id="registration-form"]/div[1]//input')
    password_input = (By.XPATH, '//*[@id="registration-form"]/div[2]//input')
    password_confirm_input = (By.XPATH, '//*[@id="registration-form"]/div[3]//input')
    reg_button = (By.XPATH, '//*[@id="registration-form"]/div[4]//button')
    error_message_create = (By.XPATH, '//*[@id="error-message"]')
    error_message_conf_password = (By.XPATH, '//*[@id="confirm-password-error-matcher"]')
    error_message_password = (By.XPATH, '//*[@id="password-error-minlength"]')
    error_message_email = (By.XPATH, '//*[@id="email-error-invalid"]')
    get_login_link = (By.XPATH, '//*[@id="error-message"]/a')
    disabled_registration_button = (By.XPATH, '//*[@id="registration-form"]/div[4]/div[1]/button[@disabled="true"]')
    error_registration_massege = (By.XPATH, '//*[@id="email-error-invalid"]')


class RegistrationPage(BasePage):
    url = '/user/registration'

    def _elements_to_wait(self):
        Wait.for_visibility(self.driver, *RegistrationPageLocators.error_message_create)


    def email_input(self, email):
        self.driver.find_element(*RegistrationPageLocators.email_input).send_keys(email)


    def password_confirm_input(self, password):
        self.driver.find_element(*RegistrationPageLocators.password_input).send_keys(password)


    def fill_password_input(self, password):
        self.driver.find_element(*RegistrationPageLocators.password_confirm_input).send_keys(password)


    def click_on_registration_button(self):
        self.driver.find_element(*RegistrationPageLocators.reg_button).click()


    def check_disabled_registration_button(self):
        try:
            self.driver.find_element(*RegistrationPageLocators.disabled_registration_button)
        except:
            print('user can not registrate with wrong data')

    def check_successful_registration(self):
        assert self.driver.find_element(*RegistrationPageLocators.error_registration_massege), 'can not reg'
