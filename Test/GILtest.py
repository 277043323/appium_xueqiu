import threading


# #主线程死循环，占满cpu
# def test():
#     while True:
#         #这是一个占位符，是一个空语句，使程序运行的时候不会出错。
#         pass

#python GIL全局解释器锁。多线程并发是假的，GIL是Cpython解释器的问题，不是python语言的问题，解释器有很多种。c语言写的解释器cpython,jpython是java写的解释器
#GIL是Cpython解释器的问题。多线程执行多任务，保证在同一个时刻只有一个线程在运行，这个就是GIL.多线程共享全局变量。多线程爬虫比单线程要快吗？是的。，GIL效率低如果是计算密集型。这个时候用多进程
#IO密集型，这个使用多线程是可以省时间的。


# t1 = threading.Thread(target=test)
# t1.start()
# a=[11]
#
# a=[11,22,33]
# b=a
# print(a)
# print(b)
# print(id(a))
# print(id(b))
#
# #a,b的id值是一样的。直接打印的值也是一样的。这其实就是一个赋值语句，这个也是浅拷贝，指向的是引用
import copy
# #深拷贝。拷贝所有的值，若被拷贝的值变化时，拷贝后的值不受影响
# c=copy.deepcopy(a)
# print(c)
# print(id(c))
# a.append(44)
# print(a)
# print(b)
# print(c)

a=[11,22]
b=[33,44]
c=[a,b]
d=c
#这个是浅拷贝，只拷贝了一层，更深层没有拷贝，若被拷贝的里层值变了，拷贝后的值也会变化，
e=copy.copy(c)
print(c)
print(d)
print(id(e))
print(id(c))
c[0].append(55)
print(c)
print(e)
#copy.copy拷贝的是元组，那么它不会进行浅拷贝，仅仅是指向。
#原因：因为元组是不可变类型，那么意味着数据一定不能修改，因此copy.copy的时候它自动的判断，如果是元组他就只指向。
#此时id是一样的。deepcopy的时候也是一样的。
#如果用copy.copy，copy.deepcopy对一个全部都是不可变类型的数据进行拷贝，那么他们结果相同，都是引用指向。如果拷贝的是一个拥有可变类型的数据，那么deepycopy是深拷贝
#copy是使用
f=b[:]
print(id(f))
#切片.也是属于浅拷贝。
