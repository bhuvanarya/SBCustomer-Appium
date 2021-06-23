import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, \
    NoSuchElementException, InvalidElementStateException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'Arya'
desired_caps['app'] = ('G:/Appium/sbfran.apk')
desired_caps['appPackage'] = 'com.shopbox.franchisee'
desired_caps['appActivity'] = 'com.shopbox.franchisee.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(1)
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException,InvalidElementStateException])
'''
#driver.find_element_by_android_uiautomator('text("Phone number")').click()
#time.sleep(1)
ele = wait.until(lambda x: x.find_element_by_class_name("android.widget.EditText"))
ele.click()
ele.send_keys("9880308886")
#driver.find_element_by_class_name("android.widget.EditText").send_keys("9880308886")
time.sleep(5)
'''
#element=driver.find_element_by_xpath("//android.widget.EditText[@text='Phone number']")
username = driver.find_element_by_android_uiautomator('text("Phone number")')
username.click()

actions = ActionChains(driver)
actions.send_keys("9880308886")
#actions.send_keys_to_element(element, "9880308886")
actions.perform()

password = driver.find_element_by_android_uiautomator('text("Password")')
password.click()

actions = ActionChains(driver)
actions.send_keys("shop@2021")
#actions.send_keys_to_element(element, "9880308886")
actions.perform()

# element.click()
#element.send_keys("9880308886")
driver.find_element_by_accessibility_id("Login").click()

time.sleep(10)

driver.find_elements_by_xpath()