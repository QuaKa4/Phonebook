from helpers.login_test_helper import login_test_helper
from pages.information_contact_page import InformationPage
from pages.main_page import MainPage


def test_create_edit_delete_contact(driver):
    login_test_helper(driver)
    main_page = MainPage(driver)
    main_page.contact_add_button_press()
    main_page.contact_name_input_sendkeys()
    main_page.contact_surname_input_sendkeys()
    main_page.contact_submit_button_press()
    main_page.navigate_to_url()

    main_page.delete_contact_button_press()
    main_page.delete_contact_checkbox_press()
    main_page.delete_contact_submit_button_press()
    main_page.check_deleted_contact()
    main_page.navigate_to_url()

    information_page = InformationPage(driver)
    information_page.navigate_to_url()
    information_page.contact_edit_button_press()
    information_page.contact_edit_input_sendkeys()
    information_page.contact_edit_submit_button_press()
    driver.quit()


