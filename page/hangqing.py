from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage
from page.jiaoyi import Jaoyi


class Hangqing(BasePage):
    def goto_jiaoyi(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="北京君正"]').click()
        return Jaoyi(self.driver)

