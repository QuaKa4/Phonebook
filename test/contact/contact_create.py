from helpers.login_test_helper import login_test_helper
from pages.main_page import MainPage


def test_create_contact(driver):
    login_test_helper(driver)
    main_page = MainPage(driver)
    main_page.create_contact()
    driver.quit()
