from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from helpers.waiter import Wait
from pages.common import Exceptions


class MainPageLocators:
    main_page_hearer = (By.XPATH, '//app-home-page//app-contacts/div[1]')
    contact_add_button = (By.XPATH, '//app-header/nav/div/ul/li[2]/a')
    create_contact_name_input = (By.XPATH, '//*[@id="form-name"]')
    create_contact_surname_input = (By.XPATH, '//*[@id="form-lastName"] ')
    create_contact_submit_button = (By.XPATH, '//*[@id="add-contact-form"]/div[4]/*[@class="btn btn-primary"]')
    contact_delete_button = (By.XPATH, '//*[@id="contacts-list"]/div[1]/app-contact-item/div/button[2]')
    contact_delete_checkbox = (By.XPATH, '//*[@id="check-box-remove-contact"]')
    contact_remove_submit_button = (By.XPATH, '//*[@id="submit-remove"]')
    contact_deleted_message = (By.XPATH, '//*[@id="pop-up-success-removed-contact"]')
    contact_menu_button = (By.XPATH, '//*[@id="contacts-list"]/div[1]//button[1]')
    contact_edit_button = (By.XPATH, '//*[@id="btn-edit-contact"]')
    contact_edit_name_input = (By.XPATH, '//*[@id="edit-contact-form"]//div[@class="row"][1]//input')
    edit_contact_submit_button = (By.XPATH, '//*[@id="edit-contact-form"]//*[@type="submit"]')


class MainPage(BasePage):
    url = '/contacts'

    def _elements_to_wait(self):
        Wait.for_visibility(self.driver, *MainPageLocators.main_page_hearer)

    def contact_add_button_press(self):
        contact_add_button = self.driver.find_element(*MainPageLocators.contact_add_button)
        contact_add_button.click()

    def contact_name_input_sendkeys(self):
        create_contact_name_input = self.driver.find_element(*MainPageLocators.create_contact_name_input)
        create_contact_name_input.send_keys('some_name')

    def contact_surname_input_sendkeys(self):
        create_contact_surname_input = self.driver.find_element(*MainPageLocators.create_contact_surname_input)
        create_contact_surname_input.send_keys('some_surname')

    def contact_submit_button_press(self):
        create_contact_submit_button = self.driver.find_element(*MainPageLocators.create_contact_name_input)
        create_contact_submit_button.click()

    def delete_contact_button_press(self):
        contact_delete_button = self.driver.find_element(*MainPageLocators.contact_delete_button)
        contact_delete_button.click()

    def delete_contact_checkbox_press(self):
        contact_delete_checkbox = self.driver.find_element(*MainPageLocators.contact_delete_checkbox)
        contact_delete_checkbox.click()

    def delete_contact_submit_button_press(self):
        contact_remove_submit_button = self.driver.find_element(*MainPageLocators.contact_remove_submit_button)
        contact_remove_submit_button.click()

    def check_deleted_contact(self):
        try:
            self.driver.find_element(*MainPageLocators.contact_deleted_message)
        except Exceptions:
            raise Exceptions('Contact was not deleted')

    def click_on_created_contact_row(self):
        contact_button_menu = self.driver.find_element(*MainPageLocators.contact_menu_button)
        contact_button_menu.click()


