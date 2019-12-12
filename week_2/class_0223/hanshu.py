# -*- coding: utf-8 -*-
# @Time:2019/10/31 0031 14:39
# @Author:cp
# @Email:1171954100@qq.com
# @File:hanshu.py
#
# def say_hello():
#     print("早上好!!!")
#     # return [1,2,3]
#     return {"name":"summer","age":"18","height":"170"}
# #x,y,z =say_hello()            #默认是拿到字典中的key的值，也就是name，age，height的值
# x,y,z =say_hello().values()   #这样就是拿到values的值，也就是summer，18,170的值
# print(x)
# print(y)
# print(z)

#参数类型：位置参数  默认参数  动态参数*args  关键字参数**kwargs
#参数个数：0或者无数个
#函数体
#return  是否有返回值
# def add(x,y):         #调用函数的时候传参    形参/位置参数
#     '''加法，求任何两个值的和，并返回计算结果'''
#     print("x的值是",x)
#     print("y的值是",y)
#     return x+y

#位置参数
# res=add(3,4)            #调用函数的时候传的参数--实参--默认是按顺序赋值
# res=add(y=4,x=3)        #指定赋值,不关注顺序，指定什么就是什么
# print("计算的结果是:{}".format(res))


#默认参数：在定义函数的时候，给某个参数设置默认值
#位置参数必须在默认参数之前  def add(x,z,y=9)
# #有几个位置参数  就必须要传几个参数
# def add(x,y=9):         #调用函数的时候传参    形参/位置参数
#     '''加法，求任何两个值的和，并返回计算结果'''
#     print("x的值是",x)
#     print("y的值是",y)
#     return x+y
# # res=add(10)      #因为有默认y=9，所以就可以只传一个值
# res=add(10,20)     #当然也可以有几个传几个，只是默认值会被覆盖
# print("计算的结果是:{}".format(res))

#动态参数 *args arguments  复数  指定多个---不定长参数
# def add(*args):       #参数传递到函数内部  会把所有的参数存储到一个元组
#     print(args)
#     print(type(args))
#
#     sum=0
#     for i in args:
#         sum+=i
#     print("加法的值是：{}".format(sum))
#
# add(5,6,9,10)

#关键字参数  **kwargs  key word  arguments
#参数传递进去后变成了一个字典  kwargs  指明key value
# def student_info(**kwargs):
#     print(kwargs)
# student_info(name="妞妞",age=24)
#
# def add(*args):        #定义---表示你可以传递任意多个参数
#     print("args的值是：",args)
# t=([1,2],[3,4])
# add(t)
# add(*t)      #如果你是调用的时候--解包--脱外套--脱一层  只能加一个*

def student_info(**kwargs):
    print(kwargs)
d={"age":18,"name":"summer"}
student_info(**d)
# student_info(age=18,name=sunny)
# student_info(x={"age":18,"name":"summer"})