from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestIndex:

    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': '127.0.0.1:7555',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_index(self):
        sleep(10)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='行情']").click()
        return True
