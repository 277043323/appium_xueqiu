import pytest
import yaml

from Test.Cacl import SHIli
hh = yaml.safe_load(open("jj.yaml"))
# print(hh)

# def data():
#     for i in hh:
#         yield i
#
#
# for i in data():
#     print(i)


class Test():

    def setup(self):
        self.shi = SHIli()

#这里一直理不过来,后面的参数需要注意，第一个是参数，是字符型的，第二个是参数的取值，是列表或元组，是元组的话前面的参数就有二个值
    @pytest.mark.parametrize('data', hh)
    def test(self,data):
        ret = self.shi.add(data[0], data[1])
        print(ret)


    @pytest.mark.parametrize('data01', hh)
    def test02(self,data01):
        ret01 = self.shi.div(data01[0], data01[1])
        print(ret01)


    def test03(self):
        print("未完成功能的测试")
