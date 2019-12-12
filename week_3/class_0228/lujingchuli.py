# -*- coding: utf-8 -*-
# @Time:2019/11/1 0001 18:56
# @Author:cp
# @Email:1171954100@qq.com
# @File:lujingchuli.py

#相对路径  绝对路径
#open()#打开一个文件   ../  是往上走一级
# file=open('python15.txt')        #相对路径，相对于文件本身
# print(file.read())

#C:\Python34\python.exe E:/python15/week_3/class_0228/lujingchuli.py
#绝对路径
# file=open('E:\python15\week_3\class_0228\python15.txt')
# print(file.read())
# # \t \n  \r----转义  r  R  或者是加  \

import os  #导入os模块
# path_1=os.getcwd()      #获取当前路径，不会具体到模块名，模块名可以理解为文件名
# path_2=os.path.realpath(__file__)      #__file__指的是当前文件本身
# path_3=os.path.basename(__file__)      #__file__指的是当前文件本身
# print(path_1)                          #E:\python15\week_3\class_0228
# print(path_2)                          #E:\python15\week_3\class_0228\lujingchuli.py
# print(path_3)                          #lujingchuli.py
# print(__file__)                        #E:/python15/week_3/class_0228/lujingchuli.py

path_2=os.path.realpath(__file__)  #__file__指的是文件本身
print(path_2)

#可以对路径进行切割  根据\来切割  只会切割一层
res=os.path.split(path_2)          #对路径进行处理，返回的是元组类型的数据
print(res)
#('E:\\python15\\week_3\\class_0228', 'lujingchuli.py')
#       第一个值                          第二个值

#os.mkdir(path)   path是路径字符串  新建一个文件夹
# os.mkdir(res[0]+"\python15")

new_path=os.path.join(res[0],'python15','pythonA')       #拼接路径
os.mkdir(new_path)              #新建   只能一级一级的去建立   意思就是上一级必须要有，否则无法建立
