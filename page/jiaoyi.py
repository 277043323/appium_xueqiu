from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

from page.basepage import BasePage


class Jaoyi(BasePage):
    def jaoyi(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="沪深"]')
        touchaction = TouchAction(self.driver)
        touchaction.move_to(x=0,y=1000).perform()