
import allure
import pytest

from library.lib_selenium import *


# @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
# def test_login_valid_credentials(app):
#     app.session.login('testmobile.marina@gmail.com', app.session.get_new_psw())
#     sleep(2)
#     with allure.step('Get welcome message'):
#         greeting = get_text(app.driver, app.session.greeting_xp)
#     with allure.step('Verification - valid credentials'):
#         assert greeting.split(",")[0] == "Mar"
#     app.session.logout()


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
def test_login_invalid_psw(app):
    app.session.login('testmobile.marina@gmail.com', '12345')
    sleep(2)
    with allure.step('Get error message'):
        greeting = get_text(app.driver, app.session.invalid_cred_xp)
    with allure.step('Verify error message: Warning: No match for E-Mail Address and/or Password.'):
        assert greeting.split(",")[0] == "Warning: No match for E-Mail Address and/or Password."


# @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
# def test_login_invalid_username(app):
#     app.session.login('testmobile.marina1@gmail.com', app.session.get_new_psw())
#     sleep(2)
#     with allure.step('Get error message'):
#         greeting = get_text(app.driver, app.session.invalid_cred_xp)
#     with allure.step('Verify error message: Warning: No match for E-Mail Address and/or Password.'):
#         assert greeting.split(",")[0] == "Warning: No match for E-Mail Address and/or Password."


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
def test_login_empty_info(app):
    app.session.login("", "")
    sleep(2)
    with allure.step('Get error message.'):
        greeting = get_text(app.driver, app.session.invalid_cred_xp)
    with allure.step('Verify error message: Warning: No match for E-Mail Address and/or Password.'):
        assert greeting.split(",")[0] == "Warning: No match for E-Mail Address and/or Password."
