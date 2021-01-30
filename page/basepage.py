from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    driver=None

    def __init__(self,driver:WebDriver=None):
        if self.driver is None:
            desired_caps = {
                'platformName': 'Android',
                'platformVersion': '6.0',
                'deviceName': '127.0.0.1:7555',
                'appPackage': 'com.xueqiu.android',
                'appActivity': '.view.WelcomeActivityAlias',
            }
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(7)
        else:
            self.driver = driver

