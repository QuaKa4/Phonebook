from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from helpers.waiter import Wait
from pages.common import Exceptions


class MainPageLocators:
    main_page_hearer = (By.XPATH, '//app-home-page//app-contacts/div[1]')
    contact_add_button = (By.XPATH, '//*[text()="Добавить новый контакт"]')
    create_contact_name_input = (By.XPATH, '//*[@id="form-name"]')
    create_contact_surname_input = (By.XPATH, '//*[@id="form-lastName"] ')
    create_contact_submit_button = (By.XPATH, '//*[@id="add-contact-form"]/div[4]/button[2]')
    contact_delete_button = (By.XPATH, '//*[@id="contacts-list"]/div[1]//button[2]')
    contact_delete_checkbox = (By.XPATH, '//*[@id="check-box-remove-contact"]')
    contact_remove_submit_button = (By.XPATH, '//*[@id="submit-remove"]')
    contact_deleted_message = (By.XPATH, '//*[@id="pop-up-success-removed-contact"]')
    contact_menu_button = (By.XPATH, '//*[@id="contacts-list"]/div[1]/app-contact-item/div/button[1]')
    contact_edit_button = (By.XPATH, '//*[@id="btn-edit-contact"]')
    contact_edit_name_input = (By.XPATH, '//*[@id="edit-contact-form"]/div[1]/div[2]/input')
    edit_contact_submit_button = (By.XPATH, '//*[@id="edit-contact-form"]/div[4]/div[2]/div/button[2]')


class MainPage(BasePage):
    url = '/contacts'

    def _elements_to_wait(self):
        Wait.for_visibility(self.driver, *MainPageLocators.main_page_hearer)

    def create_contact(self):
        contact_add_button = self.driver.find_element(*MainPageLocators.contact_add_button)
        contact_add_button.click()
        create_contact_name_input = self.driver.find_element(*MainPageLocators.create_contact_name_input)
        create_contact_name_input.send_keys('some_name')
        create_contact_surname_input = self.driver.find_element(*MainPageLocators.create_contact_surname_input)
        create_contact_surname_input.send_keys('some_surname')
        create_contact_submit_button = self.driver.find_element(*MainPageLocators.create_contact_name_input)
        create_contact_submit_button.click()

    def delete_contact(self):
        contact_delete_button = self.driver.find_element(*MainPageLocators.contact_delete_button)
        contact_delete_button.click()
        contact_delete_checkbox = self.driver.find_element(*MainPageLocators.contact_delete_checkbox)
        contact_delete_checkbox.click()
        contact_remove_submit_button = self.driver.find_element(*MainPageLocators.contact_remove_submit_button)
        contact_remove_submit_button.click()

    def contact_delete_check(self):
        try:
            self.driver.find_element(*MainPageLocators.contact_deleted_message)
        except Exceptions:
            raise Exceptions('Contact was not deleted')

    def contact_menu_button_press(self):
        contact_button_menu = self.driver.find_element(*MainPageLocators.contact_menu_button)
        contact_button_menu.click()

    def contact_edit(self):
        contact_edit_button = self.driver.find_element(*MainPageLocators.contact_edit_button)
        contact_edit_button.click()
        contact_edit_button.click()
        contact_edit_name_input = self.driver.find_element(*MainPageLocators.contact_edit_name_input)
        contact_edit_name_input.clear()
        contact_edit_name_input.send_keys('_edited')
        edit_contact_submit_button = self.driver.find_element(*MainPageLocators.edit_contact_submit_button)
        edit_contact_submit_button.click()

