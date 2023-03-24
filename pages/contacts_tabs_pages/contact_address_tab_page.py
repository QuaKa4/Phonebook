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
    address_tab = (By.XPATH, '//*[@id="navbar-contact-details"]/li[4]/a')



class ContactAddressPage(BasePage):
    contact_id = 5
    url = f'http://phonebook.telran-edu.de:8080/contacts/{contact_id}'

    def address_tab_get(self):
        self.driver.find_element(*ContactAddressPageLocators.address_tab).click()
        self.driver.find_element(*ContactAddressPageLocators.address_tab).click()

    def address_tab_add(self):
        self.driver.find_element(*ContactAddressPageLocators.tab_address_contact).click()

    def address_tab_add_add_button_click(self):
        self.driver.find_element(*ContactAddressPageLocators.add_button).click()

    def address_tab_add_country_sendkeys(self):
        address_edit_country = self.driver.find_element(*ContactAddressPageLocators.input_address_edit_country)
        address_edit_country.click()


    def address_tab_add_city_sendkeys(self):
        city = fake.city()
        input_city_edit = self.driver.find_element(*ContactAddressPageLocators.input_address_edit_city)
        try:
            input_city_edit.clear()
        except:
            pass
        input_city_edit.send_keys(city)

    def address_tab_add_index_sendkeys(self):
        index = fake.postcode()
        input_index_edit = self.driver.find_element(*ContactAddressPageLocators.input_address_edit_index)
        try:
            input_index_edit.clear()
        except:
            pass
        input_index_edit.send_keys(index)

    def address_tab_add_street_sendkeys(self):
        street = fake.street_name()
        input_street_edit = self.driver.find_element(*ContactAddressPageLocators.input_address_edit_street)
        try:
            input_street_edit.clear()
        except:
            pass
        input_street_edit.send_keys(street)

    def address_tab_add_submit_button_click(self):
        self.driver.find_element(*ContactAddressPageLocators.submit_button).click()

