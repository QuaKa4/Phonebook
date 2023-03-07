from helpers.login_test_helper import login_test_helper
from pages.main_page import MainPage


# need to merge 3 cases (create,edit,delete) in one test
def test_edit_contact(driver):
    login_test_helper(driver)
    main_page = MainPage(driver)
    main_page.wait_for_load()
    main_page.contact_menu_button_press()
    main_page.contact_edit()
    driver.quit()
