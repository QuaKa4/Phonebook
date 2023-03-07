from helpers.login_test_helper import login_test_helper
from pages.contact_page import ContactPage
from pages.main_page import MainPage


# rename test_user_can_add_email
# need add cases (edite, delete), you can write one test for 3 cases(add, edit,delete)
def test_contact_email_tab_edit(driver):
    login_test_helper(driver)
    main_page = MainPage(driver)
    main_page.contact_menu_button_press()
    contact_page = ContactPage(driver)
    contact_page.email_tab_add()
    # not check added email
    driver.quit()

# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {
# "method":"xpath","selector":"//button[text()="Добавить адрес эл. почты"]"}
# Because my application use English language)))))
