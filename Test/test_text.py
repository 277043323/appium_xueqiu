



#写一个二分法查找的的程序题，查找一个值再一个列表中，若再就返回true，不在就返回false
#
# def main(list,item):
#     p=len(list)//2
#     if list[p] ==item:
#         return True
#     elif list[p]<item:
#         return main(list[p:],item)
#     else:
#         return main(list[:p+1],item)
#
#
# if __name__ == '__main__':
#     n=[1,2,3,4,5,6,7,8]
#     i=3
#     print(main(n,i))
#
# m="shjjdd"
# #切片左包括，右不包括，切换是按照索引来的
# print(m[1:])
# print(m[:2])
# #一般我们会使用到split()函数指定分割符对列表等进行切片。

# def main(list,temp):
#     mid = len(list)//2
#     if temp==list[mid]:
#         return True
#     elif temp > list[mid]:
#         return main(list[mid:],temp)
#     else:
#         return main(list[:mid+1],temp)
#
#
# if __name__ == '__main__':
#     list=[11,22,33,44,55,66,77,88]
#     temp=33
#     print(main(list,temp))

#1.上面用到了切片知识。
#python3.6版本新增加的字面量格式化字符串，是新的格式化字符串的语法
# name='同学'
# print(f'小明{name}')
#
# #3.6版本之前是使用这种格式化的语法来格式化字符串
# print('小米%s'% name)
#
# #r表示忽略转义符的作用。
# print(r"小米\nhah")
# #匿名函数，对一些简单的语句进行封装
# y = lambda x:x*2
# print(y(2))
# m = lambda x,y,z:x+y+z
# print(m(2,3,4))
#列表按照绝对值的大小进行正序排列
# m=[1,3,-4,-6,5,-2]
# # print(sorted(list, key=lambda x:abs(x)))
# print(m.sort())
# print(m)
from datetime import datetime
from functools import wraps
from time import sleep, ctime, time
import mock

# Filename : test.py
# author by : www.runoob.com

# def recur_fibo(n):
#     """递归函数
#     输出斐波那契数列"""
#     if n <= 1:
#         return n
#     else:
#         return (recur_fibo(n - 1) + recur_fibo(n - 2))
#
#
# # 获取用户输入
# nterms = int(input("您要输出几项? "))

# 检查输入的数字是否正确
# if nterms <= 0:
#     print("输入正数")
# else:
#     print("斐波那契数列:")
#     for i in range(nterms):
#         print(recur_fibo(i))
#
# list =[1,3,4,2,5]
# # list.sort()功能是针对列表自己内部进行排序， 不会有返回值， 因此返回为None。
# print(list.sort())
# # print(list)
# #列表推导式使用。
# k=[x*x for x in list]
# y= [x for x in list if x>3]
# L=[x+j for x in range(0,5) for j in range(0,4)]
# print(y)
# print(L)

#方法一


# def main():
#     for x in range(0,5):
#         for y in range(0,5):
#             return x+y
#
#
# if __name__ == '__main__':
#     list.append(main())
#     print(list)
#
# b=set()
# print(type(b))
# c={1}
# print(type(c))
# t = {x for x in list}
# t.difference(t)
# print(type(t))
# #两种方式
# b={}
# print(type(b))

#求X的N次方
# y=lambda x,n:x**n
# print(y(2,4))

#求X的N次方
# def main(x,n):
#     s=1
#     while n>0:
#         s = x*s
#         n-= 1
#     return s
#
#
# if __name__ == '__main__':
#     print(main(5, 8))

#
# def main(n,a,b):
#     while n>0:
#         n,a,b = n,b,a+b
#         print(a+b)
#         n=n-1
#
#
# if __name__ == '__main__':
#     main(5,1,1)

# def main2(n,a,b):
#     list = []
#     while n>0:
#         a,b=b,a+b
#         list.append(a+b)
#         n=n-1
#     return list
#
#
# if __name__ == '__main__':
#
#     for i in main2(5, 1, 1):
#         sleep(2)
#         print(i)


# def main2(n,a,b):
#     while n>0:
#         a,b=b,a+b
#         yield a+b
#         n=n-1
#
# if __name__ == '__main__':
#     for i in main2(2, 1, 1):
#         sleep(2)
#         print(i)


# #求X的N次方
# def main(n,x):
#     s=1
#     while n>0:
#         s=x*s
#         n-=1
#     return s
#
#
# if __name__== '__main__':
#     print(main(3, 2))

#用递归的方式实现斐波那契数列。


# def recur_fibo(n):
#     """递归函数
#     输出斐波那契数列"""
#     if n <= 1:
#         return n
#     else:
#         return (recur_fibo(n - 1) + recur_fibo(n - 2))
#
#
# # 获取用户输入
# nterms = int(input("您要输出几项? "))
#
# # 检查输入的数字是否正确
# if nterms <= 0:
#     print("输入正数")
# else:
#     print("斐波那契数列:")
#     for i in range(nterms):
#         print(recur_fibo(i))


# def main(n):
#     a=1
#     b=1
#     while n>0:
#         print(a+b)
#         n=n-1
#         a,b=b,a+b
#
#
# if __name__ == '__main__':
#     main(4)
# name='haha'
# print('我的名字是：{}'.format(name))

# print(f'我的名字是:{name}')
#请求操作系统打开一个对象
# f = open('txtfile')
# #对对象进行读的操作
# print(f.read())
# print(type(f.read()))
# f.close()
# print(f.closed)
# #
# # with open() as f:
# #     f.read()
#这里要知道json格式的基本定义，json格式是以列表或字典组成的，或是字典+列表的格式
import json
# d =[{"sodar_query_id":"S9wQYISmCNqk5LcPzoC1yAQ","injector_basename":"sodar2","bg_hash_basename":"ohxM8fQWd8Tg0TobMPXboC059oL_QSRCokz2ODtSYiY","bg_binary":"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"}]
# print(type(d))
# print(type(json.dumps(d)))
# #dump,load这个是对文件进行操作
# #把json格式的数据，已字符串的形式写入文件中
# print(type(json.dump(d, open("haha", 'w'))))
# L=["guohongxia",1,"nihao","haha"]
# print(json.dump(L,open("haha",'w')))
# t ="[11,22,33]"
# print(json.loads(t))
# m=json.loads(t)
# print(type(json.loads(t)))
# #把文件中的字符串已json格式的数据读出来
# print(json.load(open("haha"),object_hook=None))
#笔记：对文件的操作一般就是写和读,json库对json格式进行输入输出的操作，dumps是把json格式的数据转化字符格式
#loads是把字符格式的数据已json格式输出
#
#捕获异常信息
# def main(a,b):
#
#     try:
#         print(a // b)
#     # except ZeroDivisionError:
#     #     print("除数不能为0")
#     except:
#         print("除数不能为字符串")
#     # else:
#     #     print(a//1)
#     finally:
#         print(a/1)
#
#
# if __name__ == '__main__':
#     main(3, '')


# #写一个回合制游戏
# class Demo:
#     def __init__(self,hp,power):
#         self.hp = hp
#         self.power = power
#
#     def main(self,emepy_power,emenpy_hp):
#         hp = self.hp-emepy_power
#         emenpy_hp = emenpy_hp-self.power
#         if hp<emenpy_hp:
#             print("敌人赢了")
#         elif hp<emenpy_hp:
#             print("我赢了")
#         else:
#             print("平局")
#
#     def houyi(fangwei):
#         return "我是一个装饰器"
#
#
# if __name__ == '__main__':
#     main(1000,200)

# s =[11,22,33]
#
# A = json.dumps(s)
# print(A)
# # print(type(A))
# j="[11,22,33]"
# #这个函数在服务端用的比较多，响应的数据为json格式的数据
# G = json.loads(j)
# print(type(G))

#写一个二分法查找的的程序题，查找一个值再一个列表中，若再就返回true，不在就返回false

#
# def main(n, N):
#     middle = len(N)//2
#     if N[middle] > n:
#         return main(n, N[:middle+1])
#     elif N[middle] < n:
#         return main(n, N[middle:])
#     else:
#         return n
#
#
# if __name__ == '__main__':
#     print(type(main(3, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#     print(main(3, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
#
# #
# # name='guo,hong,xia'
# # print(name.split(',')[:1])
#
# #迭代
# #给多个数进行排序
# import os
#
# print(os.getcwd())

#方法一：
# def main():
#     list = ["11","12345","123"]
#     for j in range(len(list)-1):
#         if len(list[j]) > len(list[j+1]):
#             list[j], list[j+1] = list[j+1], list[j]
#     print(list[-1])
#
# main()
# if __name__ == '__main__':
#     print(main())
#方法二：
# #
# def main(elem):
#     return elem[0]
#
# list = ["我", "我们", "你"]
# e = "".join(list)
# print(type(e))
# print(e)
# print(type(list))
# list.sort(key=main)
# print(list[-1])
# print(list)
# print(e.split("我"))
# h = "-".join(e)
# print(h)
#key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。



# 获取列表的第二个元素
# def takeSecond(elem):
#     return elem[1]


# # 列表
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]
#
# # 指定第二个元素排序
# random.sort(key=takeSecond)
#
# # 输出类别
# print('排序列表：')
# print(random)


#用递归的方式实现斐波那契数列
#递归函数有几个点是要关注的：1.首先递归函数是一个函数；2.递归函数必须有结束的条件，3.函数自己调用自己

# def fibo(n):
#     #这是一个结束的条件
#     if n<=1:
#         return n
#     else:
#         #函数自己调用自己
#         return (fibo(n-1)+fibo(n-2))
#
#
# t = int(input("请输入数字n:"))
# for i in range(t):
#     print(fibo(i))


# #实现冒泡排序
# L=[1,4,3,6,2,9,5]
#
# #3.依次得出数列中最大得数，有七个数，输出前6个数，后面一个数就不用计算所以是长度-1
# for i in range(len(L)-1):
#     # 2.把数列中的数两两进行比较，即数列有7个数，那就的共比较6次，得出数列中最大的一个数,(这里减i是对程序进行优化，每次拿出一个数后，就可以不对那个数进行比较)
#     for j in range(len(L)-1-i):
#         # 1.先比较两个数的大小，并进行排序，若前面数大就交换位置，反之则位置不变
#         if L[j]>L[j+1]:
#             L[j],L[j+1]=L[j+1],L[j]
# print(L)
# #sort函数没有返回值，但是会对列表进行排序
# L.sort(reverse=True)
# print(L)

#python 实现字符串替换
# a ="hello world"
# print(a.replace("hello", "world"))
# #比较两个字符并把相同的提取出来,这里考虑用到正则表达式,用列表推导式来得出结论
# b="abcdlk"
# c="abclf"
# n= set(c)
# m=set(b)
# n.intersection()
# print(n.intersection(m))
# l=n.intersection(m)
# z =str(l)
# print(z)


import re
#这个求出了最长公共子序列
# list =[i for i in b if i in c]
# print(list)

#求出最长公共字符串
#多进程间的通信？
# set={1,3}
# set.intersection()
# import logging
# logging.basicConfig(level=logging.INFO)
#
# def loop():
#     logging.info("start loop at"+ctime())
#     sleep(2)
#
#
# if __name__ == '__main__':
#     loop()
# # 切片和range()这个函数里面逻辑有点相似左包括右不包括[1:2:1],range(1,7,1),最后一个数为步数，默认不写都是1，前面2个数是都是根据索引来计算的。
# set = {11,22,33,44,55}
# st = "asdfg"
# list = [1,2,3,4,5,6]
# print(len(list))
# print(st.endswith('g'))   #endswith()返回的是一个布尔类型。
# t = list[:-1:]
# print(t)

# y = st[::2]
# print(y)
#
#
# mol =lambda x:x.sort()
# L=[1, 4, 2, 3]
# print(mol(L))
# print(L)
#使用匿名函数输出x的y次方
#笔记匿名函数和其他函数相比是有返回值的，不需要用命令return
# f =lambda x,y:x**y
# print(f(2,3))
#
# def main(n,x):
#     s=1
#     while n>0:
#         s=x*s
#         n-=1
#     return s
#
#
# print(main(3, 2))

# print(bool(None))

#笔记：if条件语句后面跟的是一个bool类型的条件，这个是前提若条件返回的是TRUE则条件成立，否则条件不成立。数字系统会默认的返回一个TRUE,0系统会返回FLASE,
#非空的字符串返回的都是TRUE,为空时返回的是FALSE.

#for和while都可以有else语句。那么是不是说else关键词是独立的，不是和某个符号相连的。
#迭代输出序列时（如：列表）使用 for 比 while 更好？为什么要更好呢。

#闭包，和面向对象的区别。闭包占用空间小，面向对象占用空间会比较大。闭包实现的功能简单

#
# def lin_6(k,b):
#     def create_y(x):
#         print(k*x+b)
#     return create_y
#
#
# lin_6_1 = lin_6(1,2)
# lin_6_1(0)
# lin_6_1(1)
# #
# class test:
#     def main(self):
#         return ""

#函数，闭包，对象，匿名函数
#对象：能够完成最为复杂的功能，传递是很多数据+功能
#函数：能够完成较为复杂的功能，传递的是这个函数的引用，只有功能。可以把特定功能的代码封装到一个程序内，只传递代码的功能不传递数据
#匿名函数，能够完成简单的功能，传递这个函数的引用只传递功能。当作实参传递很方便，也是封装代码，但是这个只能对功能简单的代码进行封装。
#闭包，能够实现较为复杂的功能，传递这个函数的引用传递的是这个闭包中的函数以及数据，可以给代码，还可以传给代码所需要的数据


# def test1():
#     x=100
#     def test2():
#         #用于修改闭包外面的参数此时一定要加nonlocal，或者会报错
#         nonlocal x
#         print("test2-----x=%d" % x)
#         x=200
#         print("test2-----x=%d" % x)
#
#     return test2
#
# t =test1()
# print(t())

# def html(a,b):
#     n=a+b
#     def main():
#         print("我来尝试着写一下闭包---n=%d"% n)
#     return main
#
# t=html(4,9)
#
# print(t())
#
# def index(a,b):
#     return a+b
#
# t = index(2,3)
# print(t)
#
#
# class test002:
#     def test003(self,a,b):
#         return a+b
#
# #创建一个对象，对象中有很多的方法，这样程序在执行的时候就会很消耗内存，不过这对象的引用可以实现很强大的功能。
# t  =test002()
# print(t.test003(2, 4))
#
# #闭包函数的几个要点：1.闭包是一个函数，里面在嵌套一个函数；2.闭包返回的是嵌套函数的引用（函数后面不能加小括号），3.闭包内嵌的函数可以使用外面函数的数据，4.传递闭包的引用就是传递内嵌函数的功能和函数所需的数据
#
# #1.闭包和装饰器之间的异同,难道装饰器的不同就是因为装饰器传递的数据是一个函数的引用
#
# #这个就是给某个函数添加权限的方式之一，写一个闭包作为装饰器
# #用装饰器实现函数的执行时间
# def w1(f1):
#
#     def inner(*args,**kwargs):
#         start = time()
#         print("----这是权限验证1--")
#         print("----权限验证2----")
#         #这里是对实参进行拆包，一般我们在调用一个函数的时候就应该考虑到要不要给函数传递参数
#         return f1(*args,**kwargs)
#     return inner
# #这种显示是使用了python的语法糖
# @w1  #等价于 f1=w1(f1)
# def f1():
#     print(1)
# f1()
#
# #也可以这样写。
# f1 = w1(f1)
# print(f1())
#
#
# @w1
# def f2(num):
#     pass
#
# @w1
# def f3(num,**kwargs):
#     print("打印数值",kwargs)
#
# #根据函数，都要重新修改装饰器吗？如何设计一个可以装饰任何函数的装饰器呢。有呢直接把参数不定长参数就可以了
# #带有返回值的参数，怎么实现装饰器呢？在函数前面加个return关键词就可以变成一个通用的装饰器了。可以对各中函数进行装饰
#
# @w1
# def f4(num):
#     print("hahhh")
#     return 'ok'
#
#
# #多个装饰器对同一个函数装饰,这样的话就会先用下面的装饰器装在用上面的装饰器装。先执行上面的装饰器，在执行下面的装饰器。
# def w2(func):
#     def f2(*args,**kwargs):
#         print("装饰器er")
#         return func(*args,**kwargs)
#     return f2
#
# @w2   #相当于f5 = w2(f5)
# @w1
# def f5(num):
#     print()
#
#
# def w3(func):
#     def main(*args,**kwargs):
#         a=args[0]
#         b=args[1]
#         if a>b:
#             print("---权限验证-----")
#         else:
#             print("----权限验证2----")
#         return func(*args,**kwargs)
#     return main
#
#
# #装饰器中套装饰器，为什么用这种方式呢？
#
# @w3
# def log(a, b):
#     return a+b
#
# @w3(1)  #调用w3并且把1当作实参进行传递；然后把返回值当作装饰器对log进行装饰
# def log(a, b):
#     return a//b
#
#
# def logger(param):
#     def wrap(function):
#         """logger wrapper"""
#         @wraps(function)   #带有参数的装饰器,wraps是functools类中的一个闭包
#         def _wrap(*args,**kwargs):
#
#             print("这是一个日志文件")
#             print("这是一个日志文件")
#             return function(*args,**kwargs)
#         return _wrap
#     return wrap


#下面就是一个带有参数的装饰器的实现过程
# def set_level(params):
#     def level(funct):
#         def set_funct(*args,**kwargs):
#             if params ==1:
#                 print("权限验证1")
#             elif params == 2:
#                 print("权限验证2")
#             return funct(*args,**kwargs)
#         return set_funct
#     return level
#
#
# @set_level(1)
# def test1():
#     print("这是权限验证1的用户")
#
# test1()
#
# @set_level(2)
# def test2():
#     print("这是权限验证2的用户")
#
#
# print(test2.__name__)

#要对新来的用户设置调用函数的的权限。即实现用户1调用test1()函数执行的结果和用户2调用test1()函数执行的结果不一样。
#设计的时候要考虑到开放封闭原则，开方即可以对方式进行扩展，封闭为不能修改函数。
#想到了设计带有参数的装饰器。

#
# def set_warp(params):
#     def warp(func):
#         @wraps(func)    #@wraps(f):这个不仅仅是名字更改，注意：@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。
#         def _warp(*args, **kwargs):
#             if params>1:
#                 print("我是管理员")
#             return func(*args,**kwargs)
#         return _warp
#     return warp
#
#
# @set_warp(2)
# def test3():
#     return "是我，我是管理员用户"
#
#
# print(set_warp(2).__name__)
# print(test3.__name__)   #此时输出了是名字是_warp，并不是test3。这个要怎么解决呢，就用到了functools.warps方法。我们只需要添加一下这个代码就可以了，如上
#笔记：
#1.闭包，可以称之为一个特殊的函数，它与普通函数而言有一个更封闭的空间；它的书写格式是函数里面内套函数，外层函数返回的是内层函数的引用。实际执行的是内部函数代码，内层函数可以调用外层函数的数据。(这个数据可以是函数，int等等)
#闭包的特性,与普通函数相比，它既可以传递一段程序也可以传递数据。普通函数可以说只能传递一段程序
#装饰器，的实现原理就是使用了闭包。对函数进行装饰的闭包就叫装饰器，此时闭包传递的是参数是一个方法。装饰器，可对带参的函数，不带参的，有返回值的，和没有函数值的函数进行装饰，这个可以使用一个通用的装饰器完成
#装饰器，也有待参数的装饰器和不带参数的装饰器，他们的执行有点不一样，带参的是：先把参数作为实参传进行传递，然后把返回值作为装饰器对函数进行装饰
#装饰器就是对一个函数进行修改功能的函数，其实现原理就是闭包的原因

"""需求写一个通用的打印日志的装饰器"""
#
# def get_logger():
#     return "你好"
# LO=get_logger()
#
# def log(params):
#     def loggit(func):
#         @wraps(func)       #@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。
#         def wrap(*args,**kwargs):
#             print("当前是：{}".format(params))
#             with open(LOG,"a") as file:
#                 file.write(str(json.load(open("haha"))))
#             print("当前的用户名：{}".format(args[0]))
#             print("当前的密码是：{}".format(args[1]))
#             return func(*args,**kwargs)
#         return wrap
#     return loggit
#
#
# LOG = 'E:\\Ghx_Work_Project\\appium_xueqiu\\Test\\logtxt'
# @log("登陆模块的日志")   ##调用log并且把"登陆模块的日志"当作实参进行传递；然后把返回值当作装饰器对logger进行装饰.所以我们只需要在装饰器外套一个带参数的函数，并返回装饰器的名称即可。
# def logger(username,password):
#     print("当前的日志为。。。。")
#     t = open(LOG,"r")
#     print(t.read())
#
#
# print(logger("guohongxia","000111"))
#
# jsdlak="123 456"
# print(jsdlak.split(" "))
# name="你好"
# print(f"jsdlak{name}")

#接口测试自动化，于接口测试相比，自动化的用例一定是要有断言的。在写接口测试自动化时，pytest+requests，我们要考虑对requests框架进行封装,实际上我们市场上httprunner,
# 类似于dsl，这个和数据库中的dsl是一样的？
#利用po思想进行对接口测试用例进行封装：这个实际上和selenium UI自动化测试是一样的。
#为什么做接口测试，接口测试的效率更高，成本比UI测试来说更低

# def main(t):
#     for i in list(h):
#         for j in range(len(i)-1):
#             if i[j]==i[j+1]:
#
#                 return i
#             else:
#                 main(t)
#
#
#         print(i)
#
#
#
#
# t = input("请输入你的数对，并以空格分割每个数对：")
# h = t.split(' ')
# print(main(t))

# mo=[1,2,3,4]
# print(mo[-1])


# # #去除相邻重复的数,
# def quchong(S):
#     str1=[""]
#     for i in S:
#         if i == str1[-1]:
#             str1.pop()
#         else:
#             str1.append(i)
#     print(''.join(str1))
#
#
# quchong("aaahx")

#
# def quchong(S):
#     str1=[""]
#     for i in S:
#         if i==str1[-1]:
#             str1.pop()
#         else:
#             str1.append(i)
#     print("".join(str1))
# quchong("dddkk")


# for z in range(0,100):
#     for x in range(0,100):
#         for y in range(0, 100):
#             if x*3+y*2+0.5*z == 100 and x+y+z == 100:
#                 print(x, y, z)
#
#
# # # #乘法口诀表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(i)+"*"+str(j)+"="+str(i*j),end=" ")
#     print()   #这表示转行的意思


