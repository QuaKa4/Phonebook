from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ContactPageLocators:
    tab_phone_contact = (By.XPATH, '//*[@id="navbar-contact-details"]/li[2]/a')
    tab_email_contact = (By.XPATH, '//*[@id="navbar-contact-details"]/li[3]/a')
    tab_address_contact = (By.XPATH, '//*[@id="navbar-contact-details"]/li[4]/a')

    add_phone_button = (By.XPATH, '//button[text()="Добавить номер телефона"]')
    add_email_button = (By.XPATH, '//button[text()="Добавить адрес эл. почты"]')
    add_address_button = (By.XPATH, '//button[text()="Добавить адрес"]')

    input_email_edit = (By.XPATH, '//*[@id="input-email"]')
    input_phone_edit = (By.XPATH, '//*[@id="selected-cc"]')
    input_address_edit_country = (By.XPATH, '//*[@id="cc-select"]')
    input_address_edit_city = (By.XPATH, '//*[@id="input-city"]')
    input_address_edit_index = (By.XPATH, '//*[@id="input-zip"]')
    input_address_edit_street = (By.XPATH, '//*[@id="input-street"]')

    submit_button = (By.XPATH, '//*[text()=" Сохранить "]')


class ContactPage(BasePage):
    id = 2064
    url = f'http://phonebook.telran-edu.de:8080/contacts/{id}'

    def email_tab_add(self):
        email_contact_tab = self.driver.find_element(*ContactPageLocators.tab_email_contact)
        email_contact_tab.click()
        add_email_button = self.driver.find_element(*ContactPageLocators.add_email_button)
        add_email_button.click()
        input_email_edit = self.driver.find_element(*ContactPageLocators.input_email_edit)
        input_email_edit.clear()
        input_email_edit.send_keys('SomeEmail@ya.ru')
        submit_email_button = self.driver.find_element(*ContactPageLocators.submit_button)
        submit_email_button.click()

    def phone_tab_add(self):
        phone_contact_tab = self.driver.find_element(*ContactPageLocators.tab_phone_contact)
        phone_contact_tab.click()
        add_phone_button = self.driver.find_element(*ContactPageLocators.add_phone_button)
        add_phone_button.click()
        input_phone_edit = self.driver.find_element(*ContactPageLocators.input_phone_edit)
        input_phone_edit.clear()
        input_phone_edit.send_keys('83457458')
        submit_phone_button = self.driver.find_element(*ContactPageLocators.submit_button)
        submit_phone_button.click()

    def address_tab_add(self):
        address_contact_tab = self.driver.find_element(*ContactPageLocators.tab_address_contact)
        address_contact_tab.click()
        add_address_button = self.driver.find_element(*ContactPageLocators.add_address_button)
        add_address_button.click()
        input_country_edit = self.driver.find_element(*ContactPageLocators.input_address_edit_country)
        try:
            input_country_edit.clear()
        except:
            pass
        input_country_edit.send_keys('Germany')
        input_city_edit = self.driver.find_element(*ContactPageLocators.input_address_edit_city)
        try:
            input_city_edit.clear()
        except:
            pass
        input_city_edit.send_keys('Oktagon')
        input_index_edit = self.driver.find_element(*ContactPageLocators.input_address_edit_index)
        try:
            input_index_edit.clear()
        except:
            pass
        input_index_edit.send_keys('555333')
        input_street_edit = self.driver.find_element(*ContactPageLocators.input_address_edit_street)
        try:
            input_street_edit.clear()
        except:
            pass
        input_street_edit.send_keys('Ulitsa')
        submit_address_button = self.driver.find_element(*ContactPageLocators.submit_button)
        submit_address_button.click()

