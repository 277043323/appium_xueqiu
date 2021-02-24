import requests
import pytest

@pytest.fixture(scope="class")
def get_token():
    url = "http://10.0.0.13:8090/login"
    method = "post"
    datas={
        "username":"guohongxia",
        "password":"000111"
    }
    ret = requests.request(url=url,method=method,data=datas)
    return ret.json()["token"]