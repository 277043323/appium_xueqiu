'''下面是unittest框架的简单的应用'''
#和pytest框架相比，unittest是python自带的框架，不需要我们去手动的安装
#unittest需要手动去继承TestCase类才可以使用
#pytest框架是python的第三方框架，是需要我们手动去安装的。pytest功能更加的强大
#pytest框架是可以执行unittest代码的。
import unittest

from pytest_display.demo_pytest import Test
import sys
print(sys.path)

#在命令种添加路径
sys.path.append('..')


class Testcal(unittest.TestCase):

    def test_add_1(self):
        self.add = Test()
        result = self.add.add(1,2)
        print(result)
        self.assertEqual(3, result)
