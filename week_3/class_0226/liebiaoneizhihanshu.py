# -*- coding: utf-8 -*-
# @Time:2019/10/31 0031 19:28
# @Author:cp
# @Email:1171954100@qq.com
# @File:liebiaoneizhihanshu.py

#列表内置函数，增删改查
# L=[0.02,100,'hello',(1,2,3),['python',0.02]]

#增加：
#1）
# s=[4,5,6]
# L=L+s
# print(L)

#2) append()        #给列表里增加元素，增加在最后面
# L.append("java")  #没有返回值，直接作用于这个列表   每次只能加一个元素
# print(L)

#3)insert()
# L.insert(0,"cp")  #索引，值
# print(L)

#4)extend  拓展列表   效果与加号等效
# s=[6,7,8]
# L.extend(s)
# print(L)


#改
# L=[0.02,100,'hello',(1,2,3),['python',0.02]]
# L[0]="chen"           #其实就是赋值运算
# print(L)

#查：利用索引值  以及切片取值

#删除： pop()  默认删除最后一个元素   指定索引就删除指定位置的值
# L=[0.02,100,'hello',(1,2,3),['python',0.02]]
# res=L.pop()
# # res=L.pop(1)
# print(L)
# print("被删除的元素是:",res)
#
# L.clear()    #清空的操作

#remove(): 移除第一个遇到的值
# L=[0.02,100,'hello',(1,2,3),['python',0.02],0.02]
# L.remove(0.02)
# print(L)

#range(m,n,k):生成指定的整数序列
#m:索引头   n:索引尾    k:步长   默认值为1
#传一个参数，默认索引头是0 从0开始
# res=list(range(10))
# res=range(0)  取头不取尾，都是0，就是空
# res=list(range(0,-2))      #空的，从0开始，步长是1
# print(res)

# L=[100,'hello',(1,2,3),['python',0.02],100]
# # print(len(L))       #长度是4
# for i in range(len(L)):       #range(4)-->range(0,4,1)-->0,1,2,3
#     print(L[i])

#倒序输出
# for i in range(len(L)-1,-1,-1):   #索引值是0,1,2,3 所以需要时长度-1，取头不取尾，所以尾是-1，倒序步长是-1
#     print(L[i])

# L.clear()
# res=L.count('hello')
# res=L.copy()    #深copy  浅copy
# res=L.index(100,2)   #查找第一次出现的索引,也可以添加指定索引位置开始搜索，也可以不加
# L.reverse()        #没有返回值，列表翻转的意思，倒序
# print(L)
# print(res)





#经典冒泡排序，利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序：小的排在前面
# a=[1,7,4,89,34,2]
# a.sort()        #数字排序法
# print(a)