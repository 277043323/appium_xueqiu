import requests
import pytest
import pytest_assume
#如果把这个方法写在conftest文件中这边就可以直接引用了，不需要再次导入
# @pytest.fixture()
# def login():
#     url=""
#     data={
#
#     }
#     requests.request(method=url,data=data)

#此测试用例需要在登陆之后进行操作。
def test(login):
    url="https://www.baidu.com"
    method="post"
    ret = requests.request(method=method,url=url)
    print(ret.text)


def test01():
    pass


#pytest -m add  跳过加了标签的用例



