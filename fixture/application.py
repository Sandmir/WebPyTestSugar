from selenium import webdriver
from fixture.session import SessionHelper
from fixture.payment import PaymentHelper
from fixture.shoping_cart import ShopingHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='/Applications/Python 3.5/geckodriver')
        self.driver.implicitly_wait(20)
        self.session = SessionHelper(self)
        self.session = SessionHelper(self)
        self.shopingCart = ShopingHelper(self)
        self.payment = PaymentHelper(self)

    def open_home_page(self):
        base_url = 'https://test.sugaringfactory.com'
        self.driver.get(base_url)


    def destroy(self):
        self.driver.quit()
        # pass

