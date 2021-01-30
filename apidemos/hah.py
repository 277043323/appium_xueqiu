from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Test_ApiDemos:
    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': '127.0.0.1:7555',
            'automationName': 'UiAutomator2',
            'appPackage': ' com.xunmeng.pinduoduo',
            'appActivity': '.login.PhoneLoginActivity',
            'dontStopAppOnReset': True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def testapidemo(self):
        self.driver.implicitly_wait(4)

        self.driver.find_element(MobileBy.XPATH,"//*[@text='请输入手机号码']").send_keys("12345678901")

        self.driver.find_element(MobileBy.ID,'android:id/title').click()
        print(self.driver.page_source)
        print(self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text)