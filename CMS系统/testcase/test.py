import allure

from CMS系统.public.api_ import Api
import yaml
import pytest

print(yaml.safe_load(open("../config_/datas.yaml")))


class TestApi():
    def setup(self):
        self.Api=Api()

    @pytest.mark.parametrize("datas",yaml.safe_load(open("../config_/datas.yaml")))
    def test_school_list(self,datas):
        hh = self.Api.get_schools(url=datas["url"],method=datas["method"],login="login")
        print(hh["message"])
        assert "获取成功" == hh["message"]

    @allure.step("登陆操作")
    def test_login(self):
        tt = self.Api.login()
        print(type(tt["status"]))
        # status时直接抛出异常
        if int(tt["status"]) == 1001:
            raise Exception("这是一个登陆失败异常")

