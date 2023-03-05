from helpers.login_test_helper import login_test_helper
from pages.main_page import MainPage


# need to merge 3 cases (create,edit,delete) in one test
def test_delete_contact(driver):
    login_test_helper(driver)
    main_page = MainPage(driver)
    main_page.delete_contact()
    main_page.contact_delete_check()
    driver.quit()
