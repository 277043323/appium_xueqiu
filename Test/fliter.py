#迭代，在原来的基础上得到新得东西

#列表，字符串，元组，集合。这些数据类型是可以迭代的


from collections import Iterable
from collections import Iterator
#
#
# def main():
#     name = isinstance([11,22,33],Iterable)
#     name = isinstance([11,22,33],Iterator)
#     print(name)
#
#
# if __name__ == '__main__':
#     main()

#创建一个可迭代的对象,这个对象必须有  __iter__() 这个方法，就可以说是一个可迭代的对象，
#迭代器是有 __iter__() __next__()这两个方法的
#1.判断a是否为可迭代的对象
#2.调用iter函数获取a对象的__iter__方法的返回值
#3.__iter__方法的返回值就是一个迭代器
#4.迭代器中的值通过__next__()方法
#第一种方法，这里主要说明，可迭代的对象不一定能迭代，一定需要__next__()方法才可以迭代。

# class Classmate():
#     #__init__()这个函数是类的构造函数，它会在对象初始化的时候执行
#     def __init__(self):
#         self.names = list()
#
#     def add(self, name):
#         self.names.append(name)
#
#     def __iter__(self):
#         #__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成
#         return ClassIterator(self)
#
#
# class ClassIterator():
#     def __init__(self, obj):
#         self.obj = obj
#         print(self.obj)
#         self.mcurrent = 0
#
#     def __iter__(self):
#         pass
#
#     #__next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
#     def __next__(self):
#         if self.mcurrent <len(self.obj.names):
#             ret = self.obj.names[self.mcurrent]
#             self.mcurrent += 1
#             return ret
#         else:
#             #产生异常停止取值，防止错误。
#             raise StopIteration
#
#
# if __name__ == '__main__':
#     classmate = Classmate()
#     print(classmate)
#     print(1)
#     classmate.add("老王")
#     classmate.add("张三")
#     classmate.add("haha")
#     for i in classmate:
#         print(i)

#yield的作用可以使函数变成一个生成器


# class Man:
#
#     def __init__(self):
#         self.L = list()
#         self.mcurrent = 0
#
#     def __iter__(self):
#         return self
#
#     def add(self, name):
#         self.names= name
#         self.L.append(self.names)
#
#     def __next__(self):
#         if self.mcurrent<len(self.L):
#             print(1)
#             t = self.L[self.mcurrent]
#             #迭代器是一个可以记住遍历的位置的对象。这里是记住遍历位置的地方坐在
#             self.mcurrent+=1
#             return t
#
#         else:
#             raise StopIteration
#
#
# if __name__ == '__main__':
#     t = Man()
#     #这里说明了t是一个可迭代的对象,也是一个迭代器，可迭代的对象是可以使用通过的for语句来进行遍历的。
#     print(isinstance(t,Iterable))
#     print(isinstance(t,Iterator))
#
#     t.add("张三")
#     t.add("李四")
#     t.add("王五")
#     for i in t:
#         print(i)


#生成器
#用生成器实现斐波那契数列
#YY...我这样写就完全没有循环了,执行一下就结束了，要写一个循环语句才行

# class Test:
#     def __init__(self):
#         pass
#
#     def main(self,n):
#         self.n = n
#         i, a, b = 0, 1, 1
#         if i < self.n:
#             print(a+b)
#             i+=1
#             a,b = b,a+b
#
#
# if __name__ == '__main__':
#     t=Test()
#     t.main(10)

#改进的版本,这里用到了while循环才可啊，Python 编程中 while 语句用于循环执行程序，即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务
#
# def main(i):
#     n,a, b =0,1,3
#     while n<i:
#         print(a+b)
#         n+=1
#         a,b=b,a+b
#
#
# if __name__ == '__main__':
#     main(10)

#
#
# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
# fab(5)
#这样复用性很差,该函数返回的是None,这里又有一个知识点，有return和没return的区别，有return这个命令表示函数的结束，并且返回的是函数的执行结果，而没有
#return的函数则返回的是None，这样不利于函数的复用。好多地方用到了这个知识点
# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
# fab(5)
#改进版本，但是这个版本也有个不好的点，就是max很大是，函数会越来越占内存为此我次我们得想办法让函数运行在一个不变得内存空间里
#所以这里就想到了yield，这个函数技能返回值，又可以不用占用太多内存
def fab(max):
    n, a, b = 0, 0, 1
    L=list()
    while n < max:
        t =L.append(b)
        a, b = b, a + b
        n = n + 1
    return L


if __name__ == '__main__':
    for i in fab(5):
        print(i)

#升级版本，这里也写明了return和yield之间得区别，相同点：都可以返回函数得执行结果，不同点：return标志得是函数得结束，而yield代表得暂停执行，它会保存上次执行得所有得结果
#yield命令可以使一个函数变成一个生成器。
#还有这里也说明了生成器就是一个特殊的迭代器，并且它比迭代器更简洁


# def main(max):
#     n, a, b = 0,1,1
#     while n<max:
#         yield b
#         n+=1
#         a, b = b, a+b
#
# if __name__ == '__main__':
#
#    print(type(main(5)))
#    for i in main(5):
#         print(i)


class Man:
    def __init__(self):
        self.L =list()
        self.mcurrent = 0

    def __iter__(self):
        return self

    def add(self,name):
        self.L.append(name)

    def __next__(self):
        if self.mcurrent<len(self.L):
            #我不能直接这样写，这样函数执行到这就结束了，达不到目的
            # return self.L[self.mcurrent]
            #改进版
            t = self.L[self.mcurrent]
            self.mcurrent += 1
            return t

        else:
            raise StopIteration


if __name__ == '__main__':
    t= Man()
    t.add("hah")
    t.add("hahah")
    t.add("sjj")

    for i in t:
        print(i)
