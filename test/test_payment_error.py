import allure
import pytest
from model.credit_cart import VisaCart

from library.lib_selenium import *


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_digit_owner_field(app):
    # app.session.goto_main_store()
    app.payment.credit_cart_valid(VisaCart(owner='Tom Tom12'))
    with allure.step('Get error message'):
        actual_error = get_text(app.driver, app.payment.error_msg)
    with allure.step("Verify: Owner field doesn't accept digits"):
        assert actual_error == 'Invalid card owner name', "Owner field accept digits!! "



@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_char_cvv_field(app):
    # app.session.goto_main_store()
    app.payment.credit_cart_valid(VisaCart(cvv='12q'))
    with allure.step('Get error message'):
        actual_error = get_text(app.driver, app.payment.error_msg)
    with allure.step("Verify: CVV field doesn't accept char"):
        assert actual_error == '(TESTMODE) The card code is invalid.', "CVV field accept char!! "



@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
def test_expired_date(app):
    # app.session.goto_main_store()
    app.payment.credit_cart_valid(VisaCart(month='01', year='2017'))
    with allure.step('Get error message'):
        actual_error = get_text(app.driver, app.payment.error_msg)
    with allure.step("Verify: System doesn't accept credit carts with expired date"):
        assert actual_error == '(TESTMODE) The credit card has expired.', "System accepts credit carts with expired date!!! "
