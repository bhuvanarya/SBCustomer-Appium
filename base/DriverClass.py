from appium import webdriver


class Driver:

    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '11'
        desired_caps['deviceName'] = 'Arya'
        desired_caps['app'] = ('G:/Appium/sb-cust-test-v5.apk')
        desired_caps['appPackage'] = 'com.flex.shopbox'
        desired_caps['appActivity'] = 'com.flex.shopbox.MainActivity'

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver

