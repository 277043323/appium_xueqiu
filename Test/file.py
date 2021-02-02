import json

import yaml

L="[1,2,3,4,5]"
m=[1,2,3,4,5]

#dump是没有返回值的，没有返回类型，是对文件进行写操作的函数，
t = json.dump(L,open("haha","w"))

#dumps能把json格式数据转化为字符串型数据
print(type(json.dumps(m)))

#loads将字符串转化json格式类型
print(json.loads(L))

#json是对文件进行读操作的对象，返回的是json格式的数据
m= json.load(open("haha"))
print(type(m))

#直接使用yaml.load会提示不安全，所以我们不用这种方式
# print(yaml.load(open("jj.yaml")))
#可以用这种格式
print(yaml.load(open("jj.yaml"),Loader=yaml.FullLoader))
#对yaml文件进行读操作，
print(yaml.safe_load(open("jj.yaml")))
# yamlL={"hh":1,"jj":2}
# #对yaml文件进行写的操作
# print(yaml.dump(L, open("jj.yaml","w")))

#yaml的书写注意，空格，-表示列表

