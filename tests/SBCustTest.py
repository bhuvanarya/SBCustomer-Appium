import time
import unittest

import pytest

from base.BasePage import BasePage
from pages.SBCustPage import SBCustPage
from utilities import CustomLogger as cl



@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = SBCustPage(self.driver)
        self.bp = BasePage(self.driver)

    @pytest.mark.run(order=1)
    def test_clickOnSkip(self):
        cl.allureLogs("App Launched")
        self.cf.clickSkipButton()

    @pytest.mark.run(order=2)
    def test_clickOnDone(self):
        cl.allureLogs("Store Selection Page")
        self.cf.clickDoneButton()

    @pytest.mark.run(order=3)
    def test_getActiveStores(self):
        cl.allureLogs("Getting All data in Store selection page")
        time.sleep(2)
        Stores = self.cf.getStores()
        print(Stores[2].get_attribute("content-desc"))
        Stores[2].click()
        time.sleep(1)

    @pytest.mark.run(order=4)
    def test_changeStore(self):
        cl.allureLogs("Changing the store")
        self.cf.clickOnChangeStore()
        time.sleep(1)
        Stores = self.cf.getStores()
        print(Stores[3].get_attribute("content-desc"))
        Stores[3].click()
        time.sleep(1)

    @pytest.mark.run(order=5)
    def test_UserLogin(self):
        cl.allureLogs("User Login")
        self.cf.clickOnUserIcon()
        time.sleep(1)
        self.cf.enterPhoneNumber()
        time.sleep(1)
        self.cf.enterPassword()
        time.sleep(1)
        self.cf.clickLoginButton()
        time.sleep(1)
        self.cf.clickChangeInAlert()
        time.sleep(1)

    @pytest.mark.run(order=6)
    def test_searchProduct(self):
        cl.allureLogs("Search Product")
        self.cf.clickOnSearchtab()
        time.sleep(1)
        self.cf.enterSearchKey()
        time.sleep(1)
        self.cf.clickOnSearchSuggestion()
        time.sleep(2)

    def test_addToCart(self):
        cl.allureLogs("Add Product to cart")
        self.cf.clickOnAddtoCart()
        time.sleep(1)

    def test_openCart(self):
        cl.allureLogs("Open Cart")
        self.cf.clickOnCartIcon()
        time.sleep(1)

    def test_placeOrder(self):
        cl.allureLogs("Place order")
        self.cf.clickOnCheckOut()
        time.sleep(1)
        self.cf.clickOnPickup()
        time.sleep(1)
        self.cf.clickOnPlaceOrder()
        time.sleep(1)

    def test_cancelOrder(self):
        cl.allureLogs("Cancel Order")
        self.cf.clickOnViewOrder()
        time.sleep(1)
        self.cf.clickOnCancelOrder()
        time.sleep(1)
        self.cf.clickOnCancelOrderYes()
        time.sleep(2)
        self.bp.screenShot("cancelOrder")


