import requests

class Base:
    def requ(self, **kwargs):
        return requests.request(**kwargs)
