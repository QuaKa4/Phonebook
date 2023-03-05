from selenium.webdriver.common.by import By

from helpers.waiter import Wait
from pages.base_page import BasePage


class RegistrationPageLocators:
    email_input = (By.XPATH, '//*[@id="registration-form"]/div[1]//input')
    # Bad XPATH
    password_input = (By.XPATH, '//*[@id="registration-form"]/div[2]//input')
    # Bad XPATH
    password_confirm_input = (By.XPATH, '//*[@id="registration-form"]/div[3]//input')
    # Bad XPATH
    reg_button = (By.XPATH, '//button[text()=" Sign up "]')
    # Bad XPATH , if you use this locator with other language your test will fail
    error_message_create = (By.XPATH, '//*[@id="error-message"]')
    error_message_conf_password = (By.XPATH, '//*[@id="confirm-password-error-matcher"]')
    error_message_password = (By.XPATH, '//*[@id="password-error-minlength"]')
    error_message_email = (By.XPATH, '//*[@id="email-error-invalid"]')
    get_login_link = (By.XPATH, '//*[@id="error-message"]/a')
    disabled_button = (By.XPATH, '//*[@id="registration-form"]/div[4]/div[1]/button[@disabled="true"]')
    # rename disabled_registration_button
    # Bad XPATH


class RegistrationPage(BasePage):
    url = '/user/registration'

    def _elements_to_wait(self):
        Wait.for_visibility(self.driver, *RegistrationPageLocators.error_message_create)
    # in method _elements_to_wait should be elements which need wait before going to the page
    # bad practice wait visibility element after loaded page

    # rename fill_password_input
    def password_input(self, password):
        self.driver.find_element(*RegistrationPageLocators.password_input).send_keys(password)

    # rename fill_confirm_password_input
    def password_confirm_input(self, password):
        self.driver.find_element(*RegistrationPageLocators.password_confirm_input).send_keys(password)

    # rename fill_email_input
    def email_input(self, email):
        self.driver.find_element(*RegistrationPageLocators.email_input).send_keys(email)

    # rename click_on_registration_button
    def registration_button_press(self):
        self.driver.find_element(*RegistrationPageLocators.reg_button).click()

    # this method unused , why it you?
    def get_login_link(self):
        self.driver.find_element(*RegistrationPageLocators.get_login_link).click()

    # rename check_disabled_registration_button
    def disabled_button_check(self):
        try:
            self.driver.find_element(*RegistrationPageLocators.disabled_button)
        except:
            print('user can not registrate with wrong data')
