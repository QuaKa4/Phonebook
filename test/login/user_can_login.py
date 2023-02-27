from helpers.login_test_helper import login_test_helper


def test_user_can_login(driver):
    login_test_helper(driver)
    driver.quit()
