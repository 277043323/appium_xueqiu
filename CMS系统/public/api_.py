import pytest
import requests


class Api():
    def login(self):
        url = "http://10.0.0.13:8090/login"
        method = "post"
        headers={
            "Content-Type": "text/plain"
        }
        data={
            "username": "guohongxia",
            "password": "000111"
        }
        result = requests.request(url=url,method=method,headers=headers,data=data)
        print(result.text)
        return result.json()

    def get_schools(self,url,method,login):
        ret = requests.request(url = url,method=method)
        return ret.json()

    def loginout(self):
        pass

