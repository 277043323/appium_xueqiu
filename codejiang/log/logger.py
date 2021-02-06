from functools import wraps

import logbook
from logbook.more import ColorizedStderrHandler


def get_logger(name="接口测试"):
    print("实现的代码块")
    return get_logger(name)

LOG = get_logger()


def Logger(parmas):
    def warp(func):
        print("实现代码")
        @wraps(func)
        def _wrap(*args,**kwargs):
            print(f"{parmas}的日志问分")
            print(LOG)
            return func(*args,**kwargs)
        return _wrap
    return warp



