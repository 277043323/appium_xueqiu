import pytest

# 这个变量是用来对外暴露对象和方法的
__all__ = ['hello']
hello = 'hello world'


class Test:

    def setup(self):
        pass

    def add(self, a: int, b:int):
        return a + b

    def div(self, a, b):
        return a / b
