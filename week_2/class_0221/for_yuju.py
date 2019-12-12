# -*- coding: utf-8 -*-
# @Time:2019/10/30 0030 17:01
# @Author:cp
# @Email:1171954100@qq.com
# @File:for_yuju.py

#遍历循环：
# L=["angelababy","张嘉倪","杨幂","谢楠","柳岩"]

#for循环语法
# for 变量名 in 数据:
    #循环体
#变量包含数字，字母，下划线，但是不能以数字开头
# for item in L:               #依次按顺序访问L里面的元素，有几个元素就会循环几次
#     #在访问L里面的每一个元素的同时，会赋值给item
#     print("python牛逼！")
#     print("item的值:{}".format(item))


#到底用哪个循环？
#如果确定循环次数的话，就用for
#如果不确定循环次数，而是要达到某个限制的条件才停止，用while

#in 后面的数据类型可以是什么呢？ 字符串  字典  元组  列表
s=[]
for item in '12345':
    print(item)
    name=input("请输入你的名字")
    s.append(name)
print(s)
