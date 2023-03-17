from faker import Faker
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

fake = Faker()

class ContactPhonePageLocators:
    tab_phone_contact = (By.XPATH, '//*[@id="navbar-contact-details"]/li[2]/a')
    add_button = (By.XPATH, '//*[@id="btn-add-phone"]')
    input_phone_edit = (By.XPATH, '//*[@id="selected-cc"]')
    submit_button = (By.XPATH, '//*[@class="modal-dialog"]//*[@type="submit"]')


class ContactPhonePage(BasePage):
    contact_id = 5
    url = f'http://phonebook.telran-edu.de:8080/contacts/{contact_id}'

    def phone_tab_add_add_button_click(self):
        phone_contact_tab = self.driver.find_element(*ContactPhonePageLocators.tab_phone_contact)
        phone_contact_tab.click()

    def phone_tab_add_phone_button_click(self):
        add_phone_button = self.driver.find_element(*ContactPhonePageLocators.add_button)
        add_phone_button.click()

    def phone_tab_add_phone_input_sendkeys(self):
        phone = fake.phone()
        input_phone_edit = self.driver.find_element(*ContactPhonePageLocators.input_phone_edit)
        input_phone_edit.clear()
        input_phone_edit.send_keys(phone)

    def phone_tab_add_submit_button_click(self):
        submit_phone_button = self.driver.find_element(*ContactPhonePageLocators.submit_button)
        submit_phone_button.click()

