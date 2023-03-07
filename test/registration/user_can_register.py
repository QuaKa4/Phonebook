from pages.common import Emails, Passwords
from pages.registration_page import RegistrationPage

# test_register_new_user - that sounds better))
def test_user_can_register(driver):
    registration_page = RegistrationPage(driver)
    registration_page.navigate_to_url()
# this step needs to be done through the interface because you are not checking the intersection interface
    registration_page.password_input(Emails.EMAIL)
    registration_page.password_confirm_input(Passwords.PASSWORD)
    registration_page.email_input(Passwords.PASSWORD)
# Why in method email_input argument Passwords.PASSWORD??????? should be Emails.EMAIL
# But so that you constantly register a new user, you need to register a random email and password: example using faker
    registration_page.registration_button_press()
    registration_page.wait_for_load()
    driver.quit()
# need add check on successful register new user
# you will ask me "How", it's easy
# you have to take text from error message and write assert with actual result and expected result,
# expected result should be in code(in a variable)
