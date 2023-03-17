from faker import Faker
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
fake = Faker()


class ContactEmailPageLocators:
    tab_email_contact = (By.XPATH, '//*[@id="navbar-contact-details"]/li[3]/a')
    add_button = (By.XPATH, '//*[@id="btn-add-phone"]')
    input_email_edit = (By.XPATH, '//*[@id="input-email"]')
    submit_button = (By.XPATH, '//*[@class="modal-dialog"]//*[@type="submit"]')


class ContactEmailPage(BasePage):
    contact_id = 5
    url = f'http://phonebook.telran-edu.de:8080/contacts/{contact_id}'

    def email_tab_add_tab_button_click(self):
        email_contact_tab = self.driver.find_element(*ContactEmailPageLocators.tab_email_contact)
        email_contact_tab.click()

    def email_tab_add_add_button_click(self):
        add_email_button = self.driver.find_element(*ContactEmailPageLocators.add_button)
        add_email_button.click()

    def email_tab_add_email_input_sendkeys(self):
        email = fake.email()
        input_email_edit = self.driver.find_element(*ContactEmailPageLocators.input_email_edit)
        try:
            input_email_edit.clear()
        except:
            pass
        input_email_edit.send_keys(email)

    def email_tab_add_submit_button_click(self):
        submit_email_button = self.driver.find_element(*ContactEmailPageLocators.submit_button)
        submit_email_button.click()
