from http01.api.address import Api
from http01.log.gitlog import getlog


class TestApi(Api):
    def setup(self):
        self.Api=Api()

    @getlog("获取用户信息日志")
    def test_demo(self):
        ret =self.Api.get_info()
        print(ret)
        assert ret.status_code == 200