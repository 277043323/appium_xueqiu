import pytest
import allure
#这里容易把allure和pytest的使用混淆。这里要记录一下

from pytest_display.demo_pytest import Test


class Testcal02:
    def test(self):
        self.add_01 = Test()
        result = self.add_01.add(1,2)
        print(result)
        assert 3 ==result
