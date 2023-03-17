from faker import Faker
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

fake = Faker()


class ContactAddressPageLocators:
    tab_address_contact = (By.XPATH, '//*[@id="navbar-contact-details"]/li[4]/a')
    add_button = (By.XPATH, '//*[@id="btn-add-phone"]')
    input_address_edit_country = (By.XPATH, '//*[@id="cc-select"]')
    input_address_edit_city = (By.XPATH, '//*[@id="input-city"]')
    input_address_edit_index = (By.XPATH, '//*[@id="input-zip"]')
    input_address_edit_street = (By.XPATH, '//*[@id="input-street"]')
    submit_button = (By.XPATH, '//*[@class="modal-dialog"]//*[@type="submit"]')


class ContactAddressPage(BasePage):
    contact_id = 5
    url = f'http://phonebook.telran-edu.de:8080/contacts/{contact_id}'

    def address_tab_add(self):
        address_contact_tab = self.driver.find_element(*ContactAddressPageLocators.tab_address_contact)
        address_contact_tab.click()

    def address_tab_add_add_button_click(self):
        add_address_button = self.driver.find_element(*ContactAddressPageLocators.add_button)
        add_address_button.click()

    def address_tab_add_country_sendkeys(self):
        country = fake.country()
        input_country_edit = self.driver.find_element(*ContactAddressPageLocators.input_address_edit_country)
        try:
            input_country_edit.clear()
        except:
            pass
        input_country_edit.send_keys(country)

    def address_tab_add_city_sendkeys(self):
        city = fake.city()
        input_city_edit = self.driver.find_element(*ContactAddressPageLocators.input_address_edit_city)
        try:
            input_city_edit.clear()
        except:
            pass
        input_city_edit.send_keys(city)

    def address_tab_add_index_sendkeys(self):
        index = fake.index()
        input_index_edit = self.driver.find_element(*ContactAddressPageLocators.input_address_edit_index)
        try:
            input_index_edit.clear()
        except:
            pass
        input_index_edit.send_keys(index)

    def address_tab_add_street_sendkeys(self):
        street = fake.street()
        input_street_edit = self.driver.find_element(*ContactAddressPageLocators.input_address_edit_street)
        try:
            input_street_edit.clear()
        except:
            pass
        input_street_edit.send_keys(street)

    def address_tab_add_submit_button_click(self):
        submit_address_button = self.driver.find_element(*ContactAddressPageLocators.submit_button)
        submit_address_button.click()
