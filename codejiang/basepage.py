import selenium
import selenium.webdriver
import yaml
from selenium.webdriver.chrome.options import Options
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
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    driver=None

    # 定义一个构造函数，传一个参数进来
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self.driver = selenium.webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)

        else:
            self.driver = driver

    def find(self, locator, value):
        return self.driver.find_element(locator, value)

    def url(self, url):
        return self.driver.get(url)

    def js(self, js):
        return self.driver.execute_script(js)

    #这里封装一个显示等待的函数
    def wait_time(self, location, time):
        return WebDriverWait(self.driver, time).until(expected_conditions.invisibility_of_element(location))

    #显示等待这里也可以不用expected_conditions这个类，我们可以自己定义一个函数,下面我们定义一个匿名函数，实现的是和上面一样的
    def wait(self,location,time):
        return WebDriverWait(self.driver,time).until(lambda x:x.find_element(location))


    # def handle(self):
    #     print(self.driver.window_handles())
    #     return self.driver.window_handles[-1]

    def swith(self,n):
        self.driver.switch_to.window(self.driver.window_handles[n])

    def forward(self):
        return self.driver.forward()





