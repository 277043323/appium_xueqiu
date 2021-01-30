from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage
from page.hangqing import Hangqing


class Main(BasePage):
    def goto_hangqing(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='行情']").click()
        return Hangqing(self.driver)
        



