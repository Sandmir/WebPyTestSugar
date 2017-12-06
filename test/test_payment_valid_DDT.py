import allure
import pytest
from model.credit_cart import CreditCart
from library.lib_selenium import *

testdata = [
    ('Tom Tom', '4242424242424242', '08', '2018', '123', 'VISA'),
    ('Tom Tom', '5555555555554444', '08', '2018', '123', 'Mastercard'),
    ('Tom Tom', '5200828282828210', '08', '2018', '123', 'MastercardDebit'),
    ('Tom Tom', '378282246310005',  '08', '2018', '1234','AmericanExpress'),
    ('Tom Tom', '6011111111111117', '08', '2018', '123', 'Discover'),
    ('Tom Tom', '30569309025904',   '08', '2018', '123', 'DinersClub'),
    ('Tom Tom', '3530111333300000', '08', '2018', '123', 'JCB')
]


@pytest.mark.parametrize("owner,number,month, year, cvv, type_c", testdata)
def test_card(app, owner, number, month, year, cvv, type_c):
    app.payment.credit_cart_valid(CreditCart(owner, number, month, year, cvv, type_c))
    sleep(3)
    with allure.step('Complete order: %s' % type_c):
        assert text_is_present(app.driver, app.payment.order_added), "Payment: %s - fail!! " % type_c


