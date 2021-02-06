import json

path = '.'
get_path =path.join("/LOG")
if get_path is exit():
    path = get_path
else:
    get_path="mkdir report"


def getlog(params):
    def logger(func):
        def wraper(*args,**kwargs):
            print("这是：%s日志"% params)
            json.load(open("params","w"))
            return func(*args,**kwargs)
        return wraper
    return logger

