from page.jiaoyi import Jaoyi
from page.main import Main


class Test:
    def setup(self):
        self.main = Main()

    def test_jaoyi(self):
        self.main.goto_hangqing().goto_jiaoyi().jaoyi()

