import allure
import pytest


from library.lib_selenium import *


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_add_firs_item_to_cart(appLogin):
    quantity = 2
    if not appLogin.shopingCart.cart_empty:
        appLogin.shopingCart.remove_all_items_from_shopping_cart()
        appLogin.session.return_to_home_page()
    with allure.step('Select first item'):
        appLogin.shopingCart.select_first_item_to_cart()
    sleep(2)
    with allure.step('Add %s items to the Cart' % quantity):
        appLogin.shopingCart.add_quantity(quantity)
    with allure.step('Get quantity from the Cart'):
          cart_info = appLogin.shopingCart.get_cart_info(type ='qn')
    with allure.step('Verify quantity = %s' %quantity):
         assert quantity == cart_info, "Quantity doesn't match!!"


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
def test_prices_match(appLogin):
    quantity = 1
    if not appLogin.shopingCart.cart_empty:
        appLogin.shopingCart.remove_all_items_from_shopping_cart()
        appLogin.session.return_to_home_page()
    with allure.step('Select first item'):
        appLogin.shopingCart.select_first_item_to_cart()
    sleep(2)
    original_price  = appLogin.shopingCart.get_original_price()
    with allure.step('Add %s items to the Cart' % quantity):
        appLogin.shopingCart.add_quantity(quantity)
    with allure.step('Get price from the Cart'):
          cart_info = appLogin.shopingCart.get_cart_info()
    with allure.step('Verify prices: original price = cart price'):
         assert original_price == cart_info, "Prices doesn't match!!"


