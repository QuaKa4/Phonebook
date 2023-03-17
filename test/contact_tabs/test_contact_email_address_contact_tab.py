from faker import Faker

from helpers.login_test_helper import login_test_helper
from pages.contacts_tabs_pages.contact_address_tab_page import ContactAddressPage
from pages.contacts_tabs_pages.contact_email_tab_page import ContactEmailPage
from pages.contacts_tabs_pages.contact_phone_tab_page import ContactPhonePage

fake = Faker()

class TestContactPageCheck:
    def test_contact_email_tab(self, driver):
        login_test_helper(driver)
        contact_email_page = ContactEmailPage(driver)
        contact_email_page.navigate_to_url()
        contact_email_page.email_tab_add_tab_button_click()
        contact_email_page.email_tab_add_add_button_click()
        contact_email_page.email_tab_add_email_input_sendkeys()
        contact_email_page.email_tab_add_submit_button_click()
        driver.quit()

    def test_contact_phone_tab(self, driver):
        login_test_helper(driver)
        contact_phone_page = ContactPhonePage(driver)
        contact_phone_page.navigate_to_url()
        contact_phone_page.phone_tab_add_add_button_click()
        contact_phone_page.phone_tab_add_phone_button_click()
        contact_phone_page.phone_tab_add_phone_input_sendkeys()
        contact_phone_page.phone_tab_add_submit_button_click()
        driver.quit()

    def test_contact_address_tab(self, driver):
        login_test_helper(driver)
        contact_address_page = ContactAddressPage(driver)
        contact_address_page.navigate_to_url()
        contact_address_page.address_tab_add_add_button_click()
        contact_address_page.address_tab_add_country_sendkeys()
        contact_address_page.address_tab_add_street_sendkeys()
        contact_address_page.address_tab_add_index_sendkeys()
        contact_address_page.address_tab_add_city_sendkeys()
        contact_address_page.address_tab_add_submit_button_click()
        driver.quit()

