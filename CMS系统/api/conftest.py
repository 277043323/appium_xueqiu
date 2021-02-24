import pytest
import requests

#这个文件名是固定的，是pytest提供的，里面是放一些公共的方法
@pytest.fixture()
def login():
    url = "https://www.baidu.com"
    data = {
         "params":"你好"
    }
    requests.request(method="post",url=url, data=data)


def pytest_configure(config):
    pass

