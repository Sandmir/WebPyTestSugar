import allure
import pytest
from model.credit_cart import CreditCart

from library.lib_selenium import *

testdata = [
    ('Tom Tom12', '4242424242424242', '08', '2018', '123', 'VISA', "Owner field doesn't accept digits", 'Invalid card owner name'),
    ('Tom Tom', '5555555555554444', '08', '2018', '12q', 'Mastercard', "CVV field doesn't accept char", '(TESTMODE) The card code is invalid.'),
    ('Tom Tom', '4242424242424242', '01', '2017', '123', 'VISA', "System doesn't accept credit carts with expired date", '(TESTMODE) The credit card has expired.')
]

@pytest.mark.parametrize("owner, number,month, year, cvv, type_c, error_field, error_msg", testdata)
def test_card(app, owner, number, month, year, cvv, type_c, error_field, error_msg):
    app.payment.credit_cart_valid(CreditCart(owner, number, month, year, cvv, type_c))
    with allure.step('Get error message'):
        actual_error = get_text(app.driver, app.payment.error_msg)
    with allure.step("Verify: %s " % error_field):
        assert actual_error == error_msg, "Fail: "+ error_field



