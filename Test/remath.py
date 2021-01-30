import re
#正则表达式
# result = re.match(r"ghx","hello world")
# print(result)

# #匹配单个字符，\d匹配单个的数字，（一个0-9）
# result = re.match(r"速度与激情\d","速度与激情9")
# print(result.group())

#[12345678]==[1-8]表示数字1至8都可以，超过这个数就会报出异常

# result = re.match(r"速度与激情[1-8]","速度与激情1")
# print(result.group())

# #匹配123678跳过了45可以用如下方法去实现
# result = re.match(r"速度与激情[1-36-8]","速度与激情4")
# print(result.group())

#中括号里可以输入数字字母，一样的匹配,中括号只能匹配一个字符
# result = re.match(r"速度与激情[1-3abcd]","速度与激情as")
# print(result.group())

# result = re.match(r"速度与激情[1-3a-z]","速度与激情as")
# print(result.group())

# #\w匹配数字，字母，下划线，中文，所以这个在使用的时候要慎用
# result = re.match(r"速度与激情\w","速度与激情哈")
# print(result.group())

# #\s表示的是匹配的是空白字符,我试了一下在现在的环境下无法匹配tab键
# result = re.match(r"速度与激情\s\d","速度与激情 1")
# print(result.group())

#所有的大写的字符都和小写的字符相反

#.匹配任意的字符，这个比\w的匹配范围更广，因为他还可以匹配特殊的字符,\n换行是无法匹配的
# result = re.match(r"速度与激情.","速度与激情hjshjhsjk")
# print(result.group())
#以上所有讲的都是匹配单字符的情况

#大括号可以规定前一位的个数{1，2}表示1位2位都可以
# result = re.match(r"速度与激情\d{1,2}","速度与激情19")
# print(result.group())

#大括号可以规定前一位的个数{11}表示11位数字,若中间夹杂着非数字时，就会报错。
# result = re.match(r"速度与激情\d{11}","速度与激情12365478901")
# print(result.group())
# result = re.match(r"021-\d{8}","021-12345678")
# print(result.group())
# #？表示前面的字符可有可无
# result = re.match(r"021-?\d{8}","02112345678")
# print(result.group())

# result = re.match(r"\d{3,4}-?\d{8}","02112345678")
# print(result.group())
#*前面可有可无星号表示多个，+表示前面的字符至少一个,*匹配前一个字符出现0次或者无限次，即可有可无
# result = re.match(r"sss*$","ssss")
# print(result.group())

# #match默认是已^括号开头的，但是没有默认的结尾符号所以我们用的时候要加一个$结尾的符号，否则会出错。
# names =["name1","_name","2_name","__name__","name!","n&&&a","n"]
# for i in names:
#     res = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$",i)
#
#     if res:
#         t = res.group()
#         print("合格的变量%s"%t)
#     else:
#         print("不合格合格的变量%s"%i)
#单字符匹配\d,\w,\s,[m-n],[nmklhgd0-9_],.

# res = re.match(r"摩登家庭\d","摩登家庭1111222")
# print(res.group())

# ret = re.match(r"摩登家庭[2]","摩登家庭2")
# print(ret.group())
#[]中括号里面的数表示，表示的是匹配里面的任意一个数,re.search在一个字符串中搜索符合正则的第一个数，它返回的是一个match对象，要取的匹配或的字符串得用match对象的group()方法。
# ret = re.match("摩登家庭\s[156abdn0-9_]","摩登家庭 a")
# print(ret.group())
#{11，15}表示匹配11位或是15位
# ret = re.match(r"\d{11,15}","1235367890178")
# print(ret.group())

#{9}表示匹配9位数，匹配的是紧跟着的数
# ret = re.match(r"\d{9}","123456789")
# print(ret.group())
#?表示匹配的前面一个数可有可无
# ret = re.match(r"\d{7}_?\d{5}","1234567_12345")
# print(ret.group())

# ret = re.match(r"\d{7}_?\d{5}","123456712345")
# print(ret.group())

# name="""jjkjk
# klkl
# klkl
# kl;k
# l;
# sssss
# """
# ret = re.match(r".*",name,re.S)
# print(ret.group())


# def main():
#     names = ["name", "_name", "1name", "na%%l", "name#", "____", "j", " ", "NAkk"]
#     for i in names:
#         ret = re.match(r"[a-zA-Z_][a-zA-Z_]*$", i)
#         if ret:
#             print("符合变量%s" % ret.group())
#         else:
#             print("不符合变量%s" % i)
#
#
# if __name__ == '__main__':
#     main()

#这里要注意.这个符号，是要输入普通的字符串，所以这边要进行转义，加上\。
#如果在正则表达式中需要用到某些普通的字符，比如？.等，紧紧需要在他们面前添加一个反斜杠进行转义

# def main():
#     email = input("请输入你的邮箱地址：")
#     ret = re.match(r"[a-zA-Z_0-9]{4,20}@163\.com$",email)
#     if ret:
#         print("邮箱符合要求%s:" % ret.group())
#     else:
#         print("邮箱不符合要求%s:" % email)
#
#
# if __name__ == '__main__':
#     main()

#这里用到了分组,需要分组的用()表示。
#分组用的很广，可以使用截取出（）中的值，如需求要求截取用到了哪个邮箱。

# def main():
#     email = input("请输入你的邮箱地址：")
#     ret = re.match(r"[a-zA-Z_0-9]{4,20}@(163|126|qq)\.com$", email)
#     if ret:
#         print("邮箱符合要求:%s" % ret.group())
#     else:
#         print("邮箱不符合要求:%s" % email)
#
#
# if __name__ == '__main__':
#     main()

#判断用户用的是哪个网址。这时候我们把所有的网址取出来，然后把后面的部分取出来，这样就可以用到了分组，就可以拿到我们需要的值了。
# def main():
#     email = input("请输入你的邮箱地址：")
#     ret = re.match(r"([a-zA-Z_0-9]{4,20})@(163|126|qq)\.com$", email)
#     if ret:
#         print("邮箱符合要求:%s" % ret.group(1))
#     else:
#         print("邮箱不符合要求:%s" % email)
#
#
# if __name__ == '__main__':
#     main()
#
# html_url ="<h1>hhhjhkjhkj</h1>"
#
# ret = re.match(r"<[h][0-9]*>.*</[h][0-9]*>",html_url)
#
# print(ret.group())

#这里用到了分组的知识。也可以给分组取名称，但是这里只有\1,\2就可以了
#\1表示第一个分组，\2表示第二个分组。

# html_url ="<h1>hhhjhkjhkj</h1>"
#
# ret = re.match(r"<([h][0-9]*)>.*</\1>",html_url)
#
# print(ret.group())



# #筛选出图片：
name =' <img alt="" src="/images/476/45af839c6c7362a3ec89ca7f7e6ca53c.png"> '

# ret = re.sub(r"<img\salt=\"\"\s"," " ,name)
# print(ret)

# ret = re.sub(r"[^<|*>|&nbsp;|\n]","",name)
# print(ret)

#1.匹配以字母A开头的单词

name = "i am very fine"
ret = re.split(r" ",name)
n= str(ret)
print(n)
for i in ret:
    # print(i)
    ret1 = re.match(r"a.+",i)
    if ret1:
        print("这是包含a的单词：%s" % i )
    else:
        print("不包含a的单词：%s" % i)
ret1 = re.search(r"\ba.*\b",name)
print(ret.group())

# #匹配刚好6个字符的单词
# name = ["sssdwef","sdas","s","s32345","shkja！","AsssJs"]
# for i in name:
#  ret = re.match(r"[a-zA-Z]{6}$",i)
#  if ret:
#     print("符合:%s" %ret.group())
#
# #匹配5到12位的QQ号
# name = input("输入你的QQ号:")
# ret = re.match(r"\d{5,12}$",name)
# print(ret.group())
#
# #匹配1个或更多连续的数字
# ret = re.match(r"\d+","123124")
# print(ret.group())



