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
from time import sleep
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
# y=lambda x:x*2
# print(y(4))


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
# import json
# d =[{"sodar_query_id":"S9wQYISmCNqk5LcPzoC1yAQ","injector_basename":"sodar2","bg_hash_basename":"ohxM8fQWd8Tg0TobMPXboC059oL_QSRCokz2ODtSYiY","bg_binary":"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"}]
# print(type(d))
# print(type(json.dumps(d)))
# #dump,load这个是对文件进行操作
# #把json格式的数据，已字符串的形式写入文件中
# print(type(json.dump(d, open("haha", 'w'))))
# t ="[11,22,33]"
# print(json.loads(t))
# m=json.loads(t)
# print(type(json.loads(t)))
# #把文件中的字符串已json格式的数据读出来
# print(json.load(open("haha"),object_hook=None))
#
#
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


# def main(n,N):
#     middle = len(N)//2
#     if N[middle]>n:
#         return main(n,N[:middle+1])
#     elif N[middle]<n:
#         return main(n,N[middle:])
#     else:
#         return n
#
#
# if __name__ == '__main__':
#     print(type(main(3, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#
# name='guo,hong,xia'
# print(name.split(',')[:1])

#迭代
#给多个数进行排序
import os

print(os.getcwd())

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
#
def main(elem):
    return elem[0]

list = ["我", "我们", "你"]
e = "".join(list)
print(type(e))
print(e)
print(type(list))
list.sort(key=main)
print(list[-1])
print(list)
print(e.split("我"))
h = "-".join(e)
print(h)
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


#实现冒泡排序
L=[1,4,3,6,2,9,5]

#3.依次得出数列中最大得数，有七个数，输出前6个数，后面一个数就不用计算所以是长度-1
for i in range(len(L)-1):
    # 2.把数列中的数两两进行比较，即数列有7个数，那就的共比较6次，得出数列中最大的一个数,(这里减i是对程序进行优化，每次拿出一个数后，就可以不对那个数进行比较)
    for j in range(len(L)-1-i):
        # 1.先比较两个数的大小，并进行排序，若前面数大就交换位置，反之则位置不变
        if L[j]>L[j+1]:
            L[j],L[j+1]=L[j+1],L[j]
print(L)
#sort函数没有返回值，但是会对列表进行排序
L.sort(reverse=True)
print(L)

#python 实现字符串替换
a ="hello world"
print(a.replace("hello", "world"))










