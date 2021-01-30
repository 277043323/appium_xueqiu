import yaml


class Datas:
    def data(self):
        list =[]
        t = yaml.safe_load(open("E:\\Ghx_Work_Project\\appium_xueqiu\\codejiang\\common\\data.yaml"))
        for i in t.values():
            list.append(i)
        return list

