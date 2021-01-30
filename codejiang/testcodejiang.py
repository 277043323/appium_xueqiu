import yaml

from codejiang.basepage import Base
from codejiang.main import Main
from codejiang.index009 import Shouye
import pytest


class Test:
    def setup(self):
        self.main = Main()

    def test(self):
        self.main.goto_shouye().shouye().gonggao()



