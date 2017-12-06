import allure
import pytest
from fixture.session import receive_new_psw
from library.lib_selenium import *


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_forget_psw_negative(app):
    app.session.forget_psw("uuu")
    with allure.step('Get error message'):
        error_new_psw = get_text(app.driver, app.session.reset_error_msg)
    with allure.step('Verify error message: Warning: The E-Mail Address was not found in our records, please try again!'):
        assert error_new_psw == 'Warning: The E-Mail Address was not found in our records, please try again!'


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_forget_psw_valid(app):
    app.session.forget_psw("testmobile.marina@gmail.com")
    # with allure.step('Get message'):
    #     error_new_psw = get_text(app.driver, app.session.send_new_psw_message_xp)
    # with allure.step('Verify message: Warning: The E-Mail Address was not found in our records, please try again!'):
    #     assert error_new_psw == 'A new password has been sent to your EMail address.'
    with allure.step('Receive new PSW on email'):
        sleep(10)
        receive_new_psw()
    with allure.step("Get new PSW from email"):
        new_psw = app.session.get_new_psw()
    with allure.step('Login with new PSW'):
        wait_and_send_keys(app.driver, app.session.email_input_xp, "testmobile.marina@gmail.com")
        wait_and_send_keys(app.driver, app.session.password_input_xp, new_psw)
        wait_and_click(app.driver, app.session.login_button_xp)
    with allure.step('Get welcome message'):
        greeting = get_text(app.driver, app.session.greeting_xp)
    with allure.step('Verification - valid credentials'):
        assert greeting.split(",")[0] == "Mar"
    app.session.logout()


