# -*- coding: utf-8 -*-
# @Time:2019/10/28 0028 18:52
# @Author:cp
# @Email:1171954100@qq.com
# @File:yuanzu.py

#tuple()  元组
#1.空元组  t=()，它的类型是tuple
#2.元组里只有一个数据  t=('hello'),它的类型就是str，要加一个逗号才是元组类型
# t=()
# print(type(t))
#
# a=('hello')
# print(type(a))
#
# b=('hello',)
# print(type(b))

#3.元祖里面的元素可以是任意类型，不同元素之间用逗号隔开
# t=(1,0.02,'hello',True,(1,2,3))
# print(len(t))
# print(type(t))

#4.是有下标的，正序/反序编号都支持  取值方式同字符串
t=(1,0.02,'hello',True,(1,2,3,666,'python'))    #0,1,2,3,4  #-1，-2，-3，-4，-5

#单个取值  元组名[索引值]  正序：我想取hello  反序取True
# print(t[2])
# print(t[-1])
# 切片  元组名[索引头:索引尾:步长]  步长默认为1
# print(t[0:2:1])

#5.嵌套取值：元组里还有元组，取python里的y   层级嵌套
#首先确定目标，在t(-1)里
t=(1,0.02,'hello',True,(1,2,3,666,'python'))
print(t[-1])  #t[-1]是个元组
print(t[-1][-1])   #再在（1,2,3,666）元组里取一次t[-1]
print(t[-1][-1][1])

#元组是不可变类型  有序