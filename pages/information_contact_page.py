from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InformationPagelocators:
    contact_edit_button = (By.XPATH, '//*[@id="btn-edit-contact"]')
    contact_edit_name_input = (By.XPATH, '//*[@id="edit-contact-form"]//div[@class="row"][1]//input')
    edit_contact_submit_button = (By.XPATH, '//*[@id="edit-contact-form"]//*[@type="submit"]')


class InformationPage(BasePage):
    url = 'contacts/4182'

    def contact_edit_button_press(self):
        contact_edit_button = self.driver.find_element(*InformationPagelocators.contact_edit_button)
        contact_edit_button.click()
        contact_edit_button.click()

    def contact_edit_input_sendkeys(self):
        contact_edit_name_input = self.driver.find_element(*InformationPagelocators.contact_edit_name_input)
        contact_edit_name_input.clear()
        contact_edit_name_input.send_keys('_edited')

    def contact_edit_submit_button_press(self):
        edit_contact_submit_button = self.driver.find_element(*InformationPagelocators.edit_contact_submit_button)
        edit_contact_submit_button.click()
