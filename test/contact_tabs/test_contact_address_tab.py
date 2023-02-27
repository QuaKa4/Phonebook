from helpers.login_test_helper import login_test_helper
from pages.contact_page import ContactPage
from pages.main_page import MainPage


def test_contact_email_tab_edit(driver):
    login_test_helper(driver)
    main_page = MainPage(driver)
    main_page.contact_menu_button_press()
    contact_page = ContactPage(driver)
    contact_page.address_tab_add()
    driver.quit()
