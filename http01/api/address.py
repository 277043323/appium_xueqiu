from http01.common.base_ import Base


class Api(Base):

    def get_info(self):
        data= {
            "method": "get",
            "url": "http://10.0.0.13:8090/user/1468",

        }
        return self.requ(**data)

    def modify_info(self):
        data01={
            "method": "put",
            "url": "http://10.0.0.13:8090/weixin/user/modify/10268"
        }
        return self.requ(**data01).json()
        # print(self.requ(**data01).json())
        # assert self.requ(**data01).status_code==200





