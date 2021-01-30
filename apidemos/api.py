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
            'appPackage': 'io.appium.android.apis',
            'appActivity': 'io.appium.android.apis.view.PopupMenu1',
            'dontStopAppOnReset': True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def testapidemo(self):
        self.driver.implicitly_wait(4)

        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"Make a Popup!").click()

        self.driver.find_element(MobileBy.ID,'android:id/title').click()
        print(self.driver.page_source)
        print(self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text)


#测试用例的重要部分
#导入依赖的包，capabilities设置，初始化driver,隐式等待，增强用例的稳定性，元素定位与操作，find+action，断言assert