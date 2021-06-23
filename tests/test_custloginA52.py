import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, \
    NoSuchElementException, InvalidElementStateException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Arya'
desired_caps['app'] = ('G:/Appium/sb-cust-test-v5.apk')
desired_caps['appPackage'] = 'com.flex.shopbox'
desired_caps['appActivity'] = 'com.flex.shopbox.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(2)
wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException, InvalidElementStateException])
skip = driver.find_element_by_accessibility_id("Skip")
print(skip.get_attribute("content-desc"))
illuSkip = wait.until(lambda x: x.find_element_by_accessibility_id("Skip"))
illuSkip.click()
time.sleep(2)
illuDone = wait.until(lambda x: x.find_element_by_accessibility_id("Done"))
illuDone.click()
time.sleep(2)
# Get Stores
stores = driver.find_elements_by_class_name("android.widget.ImageView")
print(stores[2].get_attribute("content-desc"))
stores[2].click()
time.sleep(2)
changeStore = wait.until(lambda x: x.find_element_by_accessibility_id("Change store"))
changeStore.click()
time.sleep(2)
changeStores = driver.find_elements_by_class_name("android.widget.ImageView")
time.sleep(3)
print(changeStores[3].get_attribute("content-desc"))
time.sleep(1)
changeStores[3].click()

time.sleep(2)

# Login

loginIcon = wait.until(lambda x: x.find_element_by_android_uiautomator("UiSelector().index(1)"))
loginIcon.click()
time.sleep(2)
enterPhone = wait.until(lambda x: x.find_element_by_android_uiautomator('text("Phone Number")'))
enterPhone.click()
actions = ActionChains(driver)
actions.send_keys("8971393466")
actions.perform()
time.sleep(1)
driver.press_keycode(66)
enterPass = wait.until(lambda x: x.find_element_by_android_uiautomator('text("Password")'))
enterPass.click()
actions = ActionChains(driver)
actions.send_keys("123456")
actions.perform()
time.sleep(1)
driver.press_keycode(66)
time.sleep(1)
LoginButton = wait.until(lambda x: x.find_element_by_accessibility_id("Login"))
LoginButton.click()

driver.press_keycode(4)
alertChange = wait.until(lambda x: x.find_element_by_accessibility_id("Change"))
alertChange.click()
time.sleep(3)

# Search product

# searchIcon = driver.find_element_by_android_uiautomator('UiSelector().textContains("Search")')
# driver.find_element_by_xpath("//android.view.View[contains(@text='Search']").click()
# searchIcon = wait.until(lambda x: x.find_element_by_android_uiautomator('text("Search Tab 3 of 5")'))

searchIcon = driver.find_element_by_android_uiautomator('UiSelector().descriptionContains("Search")')
touch = TouchAction(driver)
touch.tap(searchIcon)
touch.perform()
time.sleep(2)
searchField = wait.until(lambda x: x.find_element_by_class_name("android.widget.EditText"))
searchField.click()
time.sleep(2)
actions = ActionChains(driver)
actions.send_keys("Dairy Milk Chocolate 6.6 gms")
actions.perform()
time.sleep(2)
searchResult = wait.until(lambda x: x.find_element_by_android_uiautomator('UiSelector().descriptionContains("Dairy")'))
touch.tap(searchResult)
touch.perform()
time.sleep(2)
# Add to cart
addtocartButtons = wait.until(lambda x: x.find_element_by_android_uiautomator('UiSelector().description("Add to cart")'))
addtocartButtons.click()
time.sleep(1)

# Open Cart

cartIcon = wait.until(lambda x: x.find_element_by_android_uiautomator("UiSelector().index(3)"))
cartIcon.click()
time.sleep(2)

# Place Order
checkOut = wait.until(lambda x: x.find_element_by_android_uiautomator('UiSelector().descriptionContains("CHECKOUT")'))
checkOut.click()
time.sleep(2)

# pickUp = wait.until(lambda x: x.find_element_by_accessibility_id("Pickup"))
touch.tap(x=70, y=420)
touch.perform()
# pickUp.click()
time.sleep(2)

# Delivery

placeOrder = wait.until(lambda x: x.find_element_by_xpath("//android.widget.Button[@content-desc='Place Order']"))
placeOrder.click()
time.sleep(2)

# View Order
viewOrder = wait.until(lambda x: x.find_element_by_accessibility_id("View Order"))
viewOrder.click()
time.sleep(2)

# Cancel Order
cancelOrder = wait.until(lambda x: x.find_element_by_accessibility_id("Cancel"))
cancelOrder.click()
time.sleep(2)
cancelOrderYes = wait.until(lambda x: x.find_element_by_accessibility_id("Yes"))
cancelOrderYes.click()

time.sleep(10)

driver.quit()
