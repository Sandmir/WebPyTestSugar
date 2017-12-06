from library.lib_selenium import *
import allure


class ShopingHelper:
    checkout_now_button = '//div[text()="Checkout now"]'
    checkout_button = '//div[text()="Checkout"]'
    accept_checkbox = '//input[@type="checkbox"]'
    confirm_button = '//div[text()="Confirm Order"]'

    cart_owner_field = '//div[text()="Card Owner"]/../input'
    cart_number_field = '//div[text()="Card Number"]/../input'
    mount_select = '//div[text()="Expiry Month"]/../select'
    year_select = '//div[text()="Expiry Year"]/../select'
    cvv_field = '//div[text()="Card Security Code (CVV2)"]/../input'

    complete_order = '//div[text()="Complete Order"]'

    error_number = "(TESTMODE) The credit cart number is invalid."
    error_owner = "Invalid card owner name"

    order_added = "Order was successfully added."

    cart_button_xp = '//a[@id="button-cart"]'
    price_class = "//div[@class = 'product-info']//span[@class = 'price-new']"

    price_cart_xp = "//span[@id = 'cart-total']"
    checkout_button_xp = '//div[text()="Checkout"]'
    remove_item_button_xp = '//div[@class="mdi mdi-minus-circle"]'
    origin_price = "//div[@class='product - info__item - special'"
    goods_free_ship_xp = "//div[div[contains(@class ,'free-shipping-marker ')]]"
    # multi_xp = "//div[text()='Please select required amount for each type:']"
    multi_xp = "//table[@class = 'product-multiselect-options-table']"
    multi_add_item = "//select[@class='product-options__multiselect-select']"

    kit_count = "//div[@class = 'product-multiselect-option-box-holder']/div[last()]"
    item_in_kit = "//div[@class = 'product-multiselect-option-box' and text() = '%s']"
    item_by_name = "//div[@class = 'name']//a[text() = '%s']"

    add_to_cart_button = "//*[text() = 'Add to Cart']"
    close_button_test = "//div[contains(@class ,'flat-button__cover')]/div[text() = 'Close']"
    items_home_page = "//div[@class = 'product-grid product-grid-home']//div[@class = 'image']"

    icons_trash = "//div[@class = 'shop-cart']//i[@class = 'icon-trash']"

    def __init__(self, app, mode='user'):
        self.app = app
        self.mode = mode

    def select_first_item_to_cart(self):
        self.app.driver.find_elements_by_xpath(self.items_home_page)[1].click()

    def select_item_to_cart_by_name(self, name):
        self.app.driver.find_element_by_xpath(self.item_by_name % name).click()

    def add_quantity(self, q=1):

        add_button = self.app.driver.find_element_by_xpath(self.cart_button_xp)

        while q > 0:
            add_button.click()

            # # this is a kit
            # try:
            #     # self.app.driver.find_element_by_xpath(
            #     #     "//div[@class='product-options__multiselect-select']").is_displayed()
            #     is_displayed(self.app.driver, "//div[@class='product-options__multiselect-select']")
            #     # print(self.app.driver.find_element_by_xpath(
            #     #     '//div[@class= "product-options__multiselect-error-status"]').text)
            #     #
            #     break
            # except:
            #     pass
            q = q - 1
            sleep(1)

    def get_original_price(self):
        with allure.step('Get original price'):
            total_cart_price = get_text(self.app.driver, self.price_class)
            cart_price = total_cart_price.split('$')[1]
            print('origine price   = ', "$" + cart_price)
            return cart_price

    def get_cart_info(self, type='price'):
        with allure.step('Get info Cart info'):
            total_cart_price = get_text(self.app.driver, self.price_cart_xp)
            if type == 'price':
                cart_info = total_cart_price.split('$')[1]
                print('cart price = ', "$" + cart_info)
            elif type == 'qn':
                cart_info = int(total_cart_price.split(' ')[0])
            return cart_info

    def remove_all_items_from_shopping_cart(self):
        with allure.step('Remove all items from the Cart'):
            driver = self.app.driver
            wait_and_click(driver, self.price_cart_xp)
            cart_items = driver.find_elements_by_xpath(self.icons_trash)
            while len(cart_items)>0:
                cart_items[0].click()
                sleep(2)
                cart_items = driver.find_elements_by_xpath(self.icons_trash)

            # for i in range(cart_items):
            #     count_xp = "//div[@class = 'paper paper_elevation-4 cart-items__item'][1]//span[@class='cart-items__item-quantity']"
            #     count_item = int(driver.find_element_by_xpath(count_xp).text[0:-1])
            #     for j in range(count_item):
            #         wait_and_click(driver, self.remove_item_button_xp)
            #     sleep(2)
            # # cart_is_empty = driver.find_element_by_xpath("//h1[text()='Your Cart is empty']").is_displayed()
            # # self.assertTrue(cart_is_empty, msg="Shopping cart is not empty!!")
            # self.app.session.return_to_home_page()
            # print('Done!! Shopping cart is empty!!')
            # print('=================================================')

    def select_items_free_ship(self):
        driver = self.app.driver
        return driver.find_elements_by_xpath(self.goods_free_ship_xp)

    @property
    def cart_empty(self):
        text_cart = get_text(self.app.driver,self.price_cart_xp)
        if text_cart == "0 item(s) $0.00":
            return True
        else:
            return False


    @property
    def multiselect_kit(self):
        try:
            return is_displayed(self.app.driver, self.multi_xp)
        except:
            return False

    def multi_item_add(self, count):
        driver = self.app.driver
        driver.find_element_by_xpath(self.item_in_kit % count).click()
        add_button = self.app.driver.find_element_by_xpath(self.cart_button_xp)
        add_button.click()


    def get_size_of_kit(self):
        driver = self.app.driver
        all_items = driver.find_elements_by_xpath(self.kit_count)
        count_str = all_items[0].text
        return int(count_str)

    def test_item(self):
        try:
            return is_displayed(self.app.driver, self.close_button_test)
        except:
            return False