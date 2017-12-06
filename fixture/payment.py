import time
import allure

from library.APIGmail import api_get_gmail
from library.lib_selenium import *


class PaymentHelper:
    checkout_now_button = '//div[text()="Checkout now"]'
    checkout_button = '//a[text()="Continue Checkout"]/..'
    accept_checkbox = '//input[@type="checkbox"]'
    confirm_button = "//button[@id ='checkout-submit-button']"

    cart_owner_field = "//input[@name = 'cc_owner']"
    cart_number_field = "//input[@name = 'cc_number']"
    mount_select = "//select[@name = 'cc_expire_date_month']"
    year_select = "//select[@name = 'cc_expire_date_year']"
    cvv_field = "//input[@name = 'cc_cvv2']"

    complete_order = "//a[@id= 'button-confirm']"

    error_number = "(TESTMODE) The credit cart number is invalid."
    error_owner = "Invalid card owner name"

    error_msg = "//*[@id='payment-error']"

    order_added = "Order was successfully added."

    def __init__(self, app):
        self.app = app

    def start_checkout(self):
        with allure.step('Click Checkout button'):
            sleep(2)
            wait_and_click(self.app.driver, self.app.shopingCart.price_cart_xp)
            sleep(3)
            wait_and_click(self.app.driver, self.checkout_button)

            # wait_and_click(self.app.driver, self.checkout_now_button)

    def submit_checkout(self):
        self.app.driver.find_element_by_xpath('//input[@name="agree"]').click()
        sleep(3)
        wait_and_click(self.app.driver, self.confirm_button)

    def fill_in_payment_info(self, cart):
        with allure.step('Fill in the Credit cart info'):
            driver = self.app.driver
            wait_and_send_keys(driver, self.cart_owner_field, cart.owner)
            wait_and_send_keys(driver, self.cart_number_field, cart.number)
            wait_and_select(driver, self.mount_select, cart.month)
            wait_and_select(driver, self.year_select, cart.year)
            wait_and_send_keys(driver, self.cvv_field, cart.cvv)

    def credit_cart_valid(self, cart):
        quantity = 2
        self.app.session.login(psw=self.app.session.get_new_psw())
        # self.app.session.return_to_home_page()
        if self.app.shopingCart.cart_empty:
            self.app.session.return_to_home_page()
            self.app.shopingCart.select_first_item_to_cart()
            sleep(2)
            with allure.step('Add %s items to the Cart' % quantity):
                self.app.shopingCart.add_quantity(quantity)
        self.app.payment.start_checkout()
        self.app.payment.submit_checkout()

        self.app.payment.fill_in_payment_info(cart)
        sleep(2)
        wait_and_click(self.app.driver, self.app.payment.complete_order)
        # with allure.step('Complete order: %s' % cart.type):
        #      assert text_is_present(self.app.driver, self.app.payment.order_added), "Payment: %s - fail!! " % cart.type
        #
