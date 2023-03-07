from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from helpers.waiter import Wait
from pages.common import Exceptions


class MainPageLocators:
    main_page_hearer = (By.XPATH, '//app-home-page//app-contacts/div[1]')
    contact_add_button = (By.XPATH, '//*[text()="Добавить новый контакт"]')
    # Bad XPATH , if you use this locator with other language your test will fail
    create_contact_name_input = (By.XPATH, '//*[@id="form-name"]')
    create_contact_surname_input = (By.XPATH, '//*[@id="form-lastName"] ')
    create_contact_submit_button = (By.XPATH, '//*[@id="add-contact-form"]/div[4]/button[2]')
    # Bad XPATH
    contact_delete_button = (By.XPATH, '//*[@id="contacts-list"]/div[1]//button[2]')
    # Bad XPATH
    contact_delete_checkbox = (By.XPATH, '//*[@id="check-box-remove-contact"]')
    contact_remove_submit_button = (By.XPATH, '//*[@id="submit-remove"]')
    contact_deleted_message = (By.XPATH, '//*[@id="pop-up-success-removed-contact"]')
    contact_menu_button = (By.XPATH, '//*[@id="contacts-list"]/div[1]/app-contact-item/div/button[1]')
    # Bad XPATH
    contact_edit_button = (By.XPATH, '//*[@id="btn-edit-contact"]')
    contact_edit_name_input = (By.XPATH, '//*[@id="edit-contact-form"]/div[1]/div[2]/input')
    # Bad XPATH
    edit_contact_submit_button = (By.XPATH, '//*[@id="edit-contact-form"]/div[4]/div[2]/div/button[2]')
    # Bad XPATH


class MainPage(BasePage):
    url = '/contacts'

    def _elements_to_wait(self):
        Wait.for_visibility(self.driver, *MainPageLocators.main_page_hearer)
    # smaller action methods need using in test
    # you have to break this method into smaller action methods
    def create_contact(self):
        contact_add_button = self.driver.find_element(*MainPageLocators.contact_add_button)
        contact_add_button.click()
        create_contact_name_input = self.driver.find_element(*MainPageLocators.create_contact_name_input)
        create_contact_name_input.send_keys('some_name')
        create_contact_surname_input = self.driver.find_element(*MainPageLocators.create_contact_surname_input)
        create_contact_surname_input.send_keys('some_surname')
        create_contact_submit_button = self.driver.find_element(*MainPageLocators.create_contact_name_input)
        create_contact_submit_button.click()

    # you have to break this method into smaller action methods
    def delete_contact(self):
        contact_delete_button = self.driver.find_element(*MainPageLocators.contact_delete_button)
        contact_delete_button.click()
        contact_delete_checkbox = self.driver.find_element(*MainPageLocators.contact_delete_checkbox)
        contact_delete_checkbox.click()
        contact_remove_submit_button = self.driver.find_element(*MainPageLocators.contact_remove_submit_button)
        contact_remove_submit_button.click()

    # rename check_deleted_contact
    def contact_delete_check(self):
        try:
            self.driver.find_element(*MainPageLocators.contact_deleted_message)
        except Exceptions:
            raise Exceptions('Contact was not deleted')

    # rename click_on_created_contact_row
    def contact_menu_button_press(self):
        contact_button_menu = self.driver.find_element(*MainPageLocators.contact_menu_button)
        contact_button_menu.click()

    # Violation of the principle PageObject
    # This method should be in ContactInfoPage(because it's a different page, it isn't MainPage)
    def contact_edit(self):
        contact_edit_button = self.driver.find_element(*MainPageLocators.contact_edit_button)
        contact_edit_button.click()
        contact_edit_button.click()
        contact_edit_name_input = self.driver.find_element(*MainPageLocators.contact_edit_name_input)
        contact_edit_name_input.clear()
        contact_edit_name_input.send_keys('_edited')
        edit_contact_submit_button = self.driver.find_element(*MainPageLocators.edit_contact_submit_button)
        edit_contact_submit_button.click()

