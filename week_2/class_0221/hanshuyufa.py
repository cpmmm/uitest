# -*- coding: utf-8 -*-
# @Time:2019/10/30 0030 19:18
# @Author:cp
# @Email:1171954100@qq.com
# @File:hanshuyufa.py

#函数定义：为了实现某个功能使用的代码段
#如果这个功能是需要重复使用的，提高复用性
#函数语法
#def 函数名(参数1，参数2，参数3)     #小写字母  不同的字母或数字之间用下划线隔开
    #'''解释文档'''
    #函数体
    #return

#参数类型：位置参数  默认参数  动态参数*args  关键字参数**kwargs
#参数个数：0或者无数个
#函数体
#return  是否有返回值

# def say_hello():
#     print("早上好！！！")
#     return None              #None是默认的返回值，不写或者没有return都是None，当然也可以将None修改成其他的
# res=say_hello()
# print("函数的返回值是：",res)
#一、
#1)函数里面没有return，它会隐形给你添加一个return None
#2)函数里面有return  但是return后面啥都没有  等同于return None
#3)函数里面有return  但是return后面加的是None  最后的结果返回None

#二、return后面只有一个值的时候，是什么类型的数据就会返回什么类型的数据
#比如说return后面整数，那么返回的就是整数类型

#三、如果return后面有多个值的时候，是以元组的类型返回
# def say_hello():
#     # print("早上好！！！")
#     return [1,2,3],{"name":"777"},"hero"
# res=say_hello()
# # print("函数的返回值是：",res)
# # print("函数的返回值是：",type(res))
# #请对say_hello()这个函数的返回结果进行遍历
# for item in res:
#     print("遍历的结果是:",item)

#四、return表示函数的结束  return后面的代码都不会执行
def add(a,b):
    res=a+b
    return res
    print(666666)


