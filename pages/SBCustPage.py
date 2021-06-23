import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.BasePage import BasePage
from utilities import CustomLogger as cl


class SBCustPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    skip = "Skip"  # Accessbility id
    done = "Done"  # Accessbility id
    stores = (By.CLASS_NAME, "android.widget.ImageView")
    changeStore = "Change store"  # Accessbility id
    userIcon = "1"  # index
    username = "Phone Number"  # text
    password = "Password"  # text
    loginbutton = "Login"  # aid
    changealert = "Change"  # aid

    def clickSkipButton(self):
        self.clickElement(self.skip, "aid")
        cl.allureLogs("Clicked on Skip Button")

    def clickDoneButton(self):
        self.clickElement(self.done, "aid")
        cl.allureLogs("Clicked on Done Button")

    def getStores(self):
        return self.driver.find_elements(*SBCustPage.stores)

    def clickOnChangeStore(self):
        self.clickElement(self.changeStore, "aid")
        cl.allureLogs("Clicked on Change store Button")

    def clickOnUserIcon(self):
        self.clickElement(self.userIcon, "index")
        cl.allureLogs("Clicked on Change store Button")

    def enterPhoneNumber(self):
        self.clickElement(self.username, "text")
        actions = ActionChains(self.driver)
        actions.send_keys("8971393466").perform()
        self.driver.press_keycode(66)
        cl.allureLogs("Entered Username")

    def enterPassword(self):
        self.clickElement(self.password, "text")
        actions = ActionChains(self.driver)
        actions.send_keys("123456").perform()
        self.driver.press_keycode(66)
        cl.allureLogs("Entered Password")

    def clickLoginButton(self):
        self.clickElement(self.loginbutton, "aid")
        time.sleep(1)
        self.driver.press_keycode(4)
        cl.allureLogs("Clicked on Login Button")

    def clickChangeInAlert(self):
        self.clickElement(self.changealert, "aid")
        cl.allureLogs("Clicked on Login Button")

    # search Product
    searchTab = "Search"  # descon
    searchfield = "android.widget.EditText" #class
    suggest = "Dairy" # descon

    def clickOnSearchtab(self):
        self.clickElement(self.searchTab, "descon")
        cl.allureLogs("Clicked on Search tab")

    def enterSearchKey(self):
        self.clickElement(self.searchfield, "class")
        actions = ActionChains(self.driver)
        actions.send_keys("Dairy Milk Chocolate 6.6 gms").perform()
        cl.allureLogs("Clicked on Search filed")

    def clickOnSearchSuggestion(self):
        self.clickElement(self.suggest, "descon")
        cl.allureLogs("Clicked on Search Suggestion")

    # Cart
    addtocart = "Add to cart"  # des
    carticon = "3"  # index

    def clickOnAddtoCart(self):
        self.clickElement(self.addtocart, "des")
        cl.allureLogs("Clicked on Add to Cart button")

    def clickOnCartIcon(self):
        self.clickElement(self.carticon, "index")
        cl.allureLogs("Clicked on Cart icon")

    # Checkout
    checkout = "CHECKOUT"  # descon
    placeorder = "//android.widget.Button[@content-desc='Place Order']"  # xpath

    def clickOnCheckOut(self):
        self.clickElement(self.checkout, "descon")
        cl.allureLogs("Clicked on CheckOut")

    def clickOnPickup(self):
        touch = TouchAction(self.driver)
        touch.tap(x=70, y=420).perform()
        cl.allureLogs("Clicked on Pickup")

    def clickOnPlaceOrder(self):
        self.clickElement(self.placeorder, "xpath")
        cl.allureLogs("Clicked on PlaceOrder")

    # Cancel Order
    viewOrder = "View Order"  # aid
    cancelorder = "Cancel"  # aid
    cancelyes = "Yes"  # aid

    def clickOnViewOrder(self):
        self.clickElement(self.viewOrder, "aid")
        cl.allureLogs("Clicked on View Order")

    def clickOnCancelOrder(self):
        self.clickElement(self.cancelorder, "aid")
        cl.allureLogs("Clicked on Cancel Button")

    def clickOnCancelOrderYes(self):
        self.clickElement(self.cancelyes, "aid")
        cl.allureLogs("Clicked on yes in Cancel alert ")

