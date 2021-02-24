import pytest
import allure
#这里容易把allure和pytest的使用混淆。这里要记录一下
#
# from pytest_display.demo_pytest import Test
# from pytest_display import demo_pytest
from pytest_display.demo_pytest import *

print(hello)

class Testcal02:
    def test(self):
        # self.add_01 = Test()
        # result = self.add_01.add(1,2)
        # print(result)
        # assert 3 ==result


        result = Test().add(1,2)
        print(result)
        assert 3 == result
# from pytest_display import demo_pytest
#
# print(demo_pytest.hello)
t = Testcal02()
print(t.test())