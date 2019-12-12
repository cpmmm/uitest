# -*- coding: utf-8 -*-
# @Time:2019/11/5 0005 10:21
# @Author:cp
# @Email:1171954100@qq.com
# @File:yichang_chu_li.py

#1.什么是异常？
#2.为什么要处理异常？
#3.怎么处理？

#print(a)         #name 'a' is not defined
#变量没有被定义，没有被赋值

#list index out of range
#索引超出有效范围，一般来说只有字符串，元组，列表有这种错误
# s=[1,2,3]
# print(s[4])

#KeyError: 'sex'
#key本身不存在，除了在字典中出现，还会在配置文件中出现
# d={'name':'summer','hobby':'it'}
# print(d['sex'])

# try:   #有冒号注意缩进，下面监控的是核心代码或者有问题的代码
#     print(a)
# except:
#     print("关闭")

#try...except...   具体的error类型  as  e（别名）
#BaseException  Exception----->从这里开始掌握，可以替代错误类型
# try:
#     print(a)
# except NameError as x:  #起一个错误类型的变量名
#     print("错误类型是:{}".format(x))

#try...except...finally
# try:
#     s=[1,2,3]
#     print(s[4])
# except Exception as e:
#     print("错误是{}".format(e))
# finally:         #不管try下面的代码是否报错，finalliy里面的代码都是会执行的
#     print("666")

#try...except...else
try:
    s=[1,2,3]
    print(s[4])
except Exception as e:
    print("错误是{}".format(e))
else:    #如果try是正确的，那下面也会执行。如果try是错误的，那么下面也不会去执行
    print(s)