from selenium import webdriver
from fixture.session import SessionHelper
from fixture.payment import PaymentHelper
from fixture.shoping_cart import ShopingHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            raise ValueError("Unrecognized browser: %s" % browser)
        self.base_url = base_url
        self.driver.implicitly_wait(20)
        self.session = SessionHelper(self)
        self.session = SessionHelper(self)
        self.shopingCart = ShopingHelper(self)
        self.payment = PaymentHelper(self)

    def open_home_page(self):
        self.driver.get(self.base_url)


    def destroy(self):
        self.driver.quit()
        # pass

