import allure
import pytest

from library.lib_selenium import *


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_prices_match_guest(app):
    quantity = 1
    app.open_home_page()
    if not app.shopingCart.cart_empty:
        app.shopingCart.remove_all_items_from_shopping_cart()
        app.session.return_to_home_page()
    with allure.step('Select first item'):
        app.shopingCart.select_first_item_to_cart()
    sleep(2)
    original_price = app.shopingCart.get_original_price()
    with allure.step('Add %s items to the Cart' % quantity):
        app.shopingCart.add_quantity(quantity)
    with allure.step('Get price from the Cart'):
        cart_info = app.shopingCart.get_cart_info()
    with allure.step('Verify prices: original price = cart price'):
        assert original_price == cart_info, "Prices doesn't match!!"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_add_firs_item_cart_guest(app):
    quantity = 2
    app.open_home_page()
    if not app.shopingCart.cart_empty:
        app.shopingCart.remove_all_items_from_shopping_cart()
        app.session.return_to_home_page()
    with allure.step('Select first item'):
        app.shopingCart.select_first_item_to_cart()
    sleep(2)
    with allure.step('Add %s items to the Cart' % quantity):
        app.shopingCart.add_quantity(quantity)
    with allure.step('Get quantity from the Cart'):
        cart_info = app.shopingCart.get_cart_info(type='qn')
    with allure.step('Verify quantity = %s' % quantity):
        assert quantity == cart_info, "Quantity doesn't match!!"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_add_item_to_cart_by_name_guest(app, name="LUXURY FANTASTIC FOUR - 172 oz / 11 lbs - SAVE 20%"):
    quantity = 1
    app.open_home_page()
    if not app.shopingCart.cart_empty:
        app.shopingCart.remove_all_items_from_shopping_cart()
        app.session.return_to_home_page()
    with allure.step('Select first item'):
        app.shopingCart.select_item_to_cart_by_name(name)
    sleep(2)
    app.shopingCart.add_quantity()
    if app.shopingCart.multiselect_kit:
        with allure.step('Add kit into the Cart'):
            sleep(1)
            item_count = app.shopingCart.get_size_of_kit()
            app.shopingCart.multi_item_add(str(item_count))
    with allure.step('Get quantity from the Cart'):
        cart_info = app.shopingCart.get_cart_info(type='qn')
    with allure.step('Verify quantity = %s' % quantity):
        assert quantity == cart_info, "Quantity doesn't match!!"
