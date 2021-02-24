import pytest

# 这个变量是用来对外暴露对象和方法的,可以写在__init__文件中，不过一般都不建议写在那个文件中，
#__all__的使用场景是，当你不想文件中的某些属性暴露时使用，暴露的属性写在这里面。当其他的文件使用from pytest_display.demo_pytest import * 的时候__all__才会生效
__all__ = ['hello','Test']
hello = 'hello world'


class Test:

    def setup(self):
        pass

    def add(self, a: int, b:int):
        return a + b

    def div(self, a, b):
        return a / b
# def f():
#     print("demo.py f()")
#
# class Demo2:
#     pass

#pytest的特色