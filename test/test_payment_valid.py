import allure
import pytest
from model.credit_cart import VisaCart, Mastercard, MastercardDebit, AmericanExpress, Discover, DinersClub, JCB
from library.lib_selenium import *


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_visa(app):
    app.payment.credit_cart_valid(VisaCart())
    sleep(3)
    with allure.step('Complete order: VISA'):
        assert text_is_present(app.driver, app.payment.order_added), "Payment: VISA - fail!! "


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_mastercard(app):
    app.payment.credit_cart_valid(Mastercard())
    with allure.step('Complete order: Mastercard'):
        assert text_is_present(app.driver, app.payment.order_added), "Payment: Mastercard - fail!! "


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_MastercardDebit(app):
    app.payment.credit_cart_valid(MastercardDebit())
    with allure.step('Complete order: MastercardDebit'):
        assert text_is_present(app.driver, app.payment.order_added), "Payment: MastercardDebit - fail!! "


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_AmericanExpress(app):
    app.payment.credit_cart_valid(AmericanExpress())
    actual_error = get_extra_info(app.driver)
    with allure.step('Complete order: AmericanExpress'):
        assert actual_error == '(TESTMODE) The merchant does not accept this type of credit card.', 'System accepts AmExp card'


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_Discover(app):
    app.payment.credit_cart_valid(Discover())
    with allure.step('Complete order: Discover'):
        assert text_is_present(app.driver, app.payment.order_added), "Payment: Discover - fail!! "


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_DinersClub(app):
    app.payment.credit_cart_valid(DinersClub())
    actual_error = get_extra_info(app.driver)
    with allure.step('Complete order: DinersClub'):
        assert actual_error == '(TESTMODE) The merchant does not accept this type of credit card.', 'System accepts DinersClub card'


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_JCB(app):
    app.payment.credit_cart_valid(JCB())
    actual_error = get_extra_info(app.driver)
    with allure.step('Complete order: JCB'):
        assert actual_error == '(TESTMODE) The merchant does not accept this type of credit card.', 'System accepts JCB card'
