import yaml

from codejiang.basepage import Base
from codejiang.main import Main
from codejiang.index009 import Shouye
import pytest
import allure


class Test:
    def setup(self):
        self.main = Main()

    # @allure.testcase("http://bug.aiiage.com:12345/zentao/testcase-view-2212-1.html",'公告栏用例（前面是用例的地址）')
    def test(self):
        self.main.goto_shouye().shouye().gonggao()

    #下面的使用场景是在测试后往往需要截图，添加图片，vedio等我们就可以在下面直接添加一段代码即可
    # def test_attact_text(self):
    #     allure.attach("这是一段纯文本",attachment_type=allure.attachment_type.TEXT)
    #
    # def test_attact_html(self):
    #     allure.attach("<body>这是一段html内容</body>",attachment_type=allure.attachment_type.HTML)
    #
    # def test_attact_photo(self):
    #     allure.attach("E:\\小将测试包\\1610425399610.png",attachment_type=allure.attachment_type.PNG)
