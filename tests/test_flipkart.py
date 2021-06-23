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
desired_caps['app'] = ('G:/Appium/sbadmin.apk')
desired_caps['appPackage'] = 'com.nxtk.warehousemanagement'
desired_caps['appActivity'] = 'com.nxtk.warehousemanagement.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(1)
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException,InvalidElementStateException])
