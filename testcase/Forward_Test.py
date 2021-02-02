from time import sleep

import allure
import selenium
from selenium import webdriver
import pytest


@allure.testcase("http://bug.aiiage.com:12345/zentao/testcase-view-2212-1.html")
@allure.feature("百度搜索")
class Test:
    def setup(self):
        self.driver = selenium.webdriver.Chrome()

    def test(self):
        with allure.step("打开百度"):
            self.driver.get("https://www.baidu.com")
        with allure.step("输入搜索词"):
            self.driver.find_element_by_id("kw").send_keys("selenium")
            self.driver.find_element_by_id("su").click()
        sleep(5)
        self.driver.forward()
        self.driver.refresh()
        with allure.step("截图保存"):
            self.driver.save_screenshot("./result/b.png")
            allure.attach.file("./result/b.png",attachment_type=allure.attachment_type.PNG)
        with allure.step("关闭浏览器"):
            self.driver.quit()


# if __name__ == '__main__':
#
#     Test().main()
