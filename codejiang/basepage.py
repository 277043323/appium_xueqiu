import selenium
import selenium.webdriver
import yaml
from selenium.webdriver.remote.webdriver import WebDriver

#这个类在调用的时候，driver连续调用了2次
# class Base:
#
#     def base(self, driver:WebDriver=None):
#         self.driver = selenium.webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(5)
#         self.driver.get("https://tea.codejiang.com/login")
#         return self.driver


class Base:

    _driver: WebDriver

    # 定义一个构造函数，传一个参数进来
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self._driver = selenium.webdriver.Chrome()
            self._driver.maximize_window()
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

    def find(self, locator, value):
        return self._driver.find_element(locator, value)

    def url(self,url):
        return self._driver.get(url)




