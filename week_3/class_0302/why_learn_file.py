# -*- coding: utf-8 -*-
# @Time:2019/11/2 0002 18:50
# @Author:cp
# @Email:1171954100@qq.com
# @File:why_learn_file.py

# def add(a,b):
#     print(a+b)
#
# file=open('python17.txt','r')
# # resp=file.readline()   #读取一行内容，返回字符串形式的数据
# resp=file.readlines()  #读取所有行数据，以列表的形式返回  每一行数据是列表一个字符串元素
# # print(resp)
#
# for i in resp:
#     i=i.strip('\n')      #移除指定字符
#     # print(type(i))
#     data=i.split(',')
#     print(data)          #变成了列表形式
#     add(int(data[0]),int(data[1]))

import requests
file=open('python18.txt','w',encoding='utf-8')
resp=requests.get('http://www.baidu.com')
file.write(resp.text)
file.close()

#1.存储测试数据   #2.可以写入我们的结果   #3.写日志  logging