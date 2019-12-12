# -*- coding: utf-8 -*-
'''
@time: 2019/11/22 0022 14:45
@author: chen
@contact: 1171954100@qq.com
@file: d7.py
@desc:
        ┏┓　　　┏┓+ +
　　　┏┛┻━━━┛┻┓ + +
　　　┃　　　　　　　┃ 　
　　　┃　　　━　　　┃ ++ + + +
　　 ████━████ ┃+
　　　┃　　　　　　　┃ +
　　　┃　　　┻　　　┃
　　　┃　　　　　　　┃ + +
　　　┗━┓　　　┏━┛
　　　　　┃　　　┃　　　　　　　　　　　
　　　　　┃　　　┃ + + + +
　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
　　　　　┃　　　┃
　　　　　┃　　　┃　　+　　　　　　　　　
　　　　　┃　 　　┗━━━┓ + +
　　　　　┃ 　　　　　　　┣┓
　　　　　┃ 　　　　　　　┏┛
　　　　　┗┓┓┏━┳┓┏┛ + + + +
　　　　　　┃┫┫　┃┫┫
　　　　　　┗┻┛　┗┻┛+ + + +

'''
#http协议
'''
请求头：user-agent，content-type
请求体：params，就是参数的意思
响应状态码：200  status-code
响应内容：status-code：200
'''
#1.给定一个列表[1,4,5,3,'a',3]，去除其中的重复元素
#命令式：
# a=[1,4,5,3,'a',3]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

#函数
# def del_repeat(a):
#     b = []
#     for i in a:
#         if i not in b:
#             b.append(i)
#     return b
#
# a=[1,4,5,3,'a',3]
# print(del_repeat(a))


#如果能用尽量少的代码解决
# a=[1,4,5,3,'a',3]
# print(list(set(a)))



#2.列表和字符串的相互转换
#（1）列表变字符串
#第一种方法
# a=['t',"2",'6','a']
# a_str=""
# for i in a:
#     a_str +=str(i)
#     a_str += '、'
# print(a_str)
# print(a_str.strip(a_str[-1]))

#第二种方法
# a=['t',"2",'6','a']
# print(" ".join(a))


#（2）字符串变成列表
# b_str="jhajkfhkjhkf"
# #定义一个空列表，进行遍历
# a=[]
# for i in b_str:
#     a.append(i)
# print(a)

#3.字符串去重，加排序
# a="ahgkaglkjalkfjlak"
# a_list=list(a)
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# b.sort()
# print(b)


#4.你的代码遇到bug，你如何处理？你在工作中遇到最困难的是，你是怎么解决的？
#技术社区，比如GitHub，stackflow，infoQ。。。
#定位问题，断点调试


#5.怎么拷贝列表     默认参数是不可变参数，列表就是可变参数
# a=['3']
# b=a
# c=a[:]
# a.append(10)
#
# print(a)    #['3',10]
# print(b)    #['3',10]
# print(c)    #[3]

#可以比较是否为同一个对象，如下所示
# a=["3"]
# print(id(a))
# b=a               #指向的是同一个对象
# print(id(b))
# c=a[:]            #拷贝一个新的对象
# print(id(c))
#
# a.append(10)
#
# print(a)
# print(b)
# print(c)


#6.单例模式的实现，只能生成一个对象的
# class A:
#     #可以理解为计划生育，只能生一个孩子==》你这个家庭之前有孩子
#     a_intance=None
#
#     def __new__(cls):   #生成对象
#        if cls.a_intance is None:
#            #没有对象的时候，生成一个新对象，给他放到类属性里来
#            cls.a_intance=super().__new__(cls)      #超继承，为什么这块使用super(),而不用A,是因为使用A之后，又回到了第134的生成对象，出现循环
#            return cls.a_intance
#        else:
#            return cls.a_intance      #如果已经有一个对象了，就返回它
#        pass
#
#     pass
#
# print(A())
# print(A())


#导入模块,也是一个单例模式，每次使用都是同一个对象
from week_8.class_0402.a import my_a
my_a


#不同对象
# class A:
#     def __init__(self):
#         pass
#
#
# print(id(A()))
# print(id(A()))
# print(id(A()))






