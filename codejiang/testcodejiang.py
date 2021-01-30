import yaml

from codejiang.basepage import Base
from codejiang.main import Main
from codejiang.index009 import Shouye
import pytest


class Test:
    def test(self):
        main = Main()
        main.goto_shouye().shouye()



