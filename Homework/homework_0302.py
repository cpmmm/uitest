# -*- coding: utf-8 -*-
# @Time:2019/11/5 0005 15:39
# @Author:cp
# @Email:1171954100@qq.com
# @File:homework_0302.py


'''有两行数据，存在txt文件里面：
url:http://47.107.168.87:8080/futureloan/mvc/api/member/register@mobile:18688773467@pwd:123456
url:http://47.107.168.87:8080/futureloan/mvc/api/member/recharge@mobile:18688773467@amount:1000
请利用上课所学知识，把txt里面的两行内容，写一个函数，返回如下格式的数据：
[{'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/register','mobile':'18688773467','pwd':'123456'},
{'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge','mobile':'18688773467','amount':'1000'}]
请自行copy数据到Python里面，进行完整的分析后，再进行程序的编写！！！！
多思考多讨论！'''

file=open('py15.txt')
resp=file.readlines()        #返回的是一个列表  每一行作为一个字符串元素
L=[]
# print(resp)
for value in resp:
    value_1=value.strip('\n')
    # print(value_1)
    value_2=value_1.split('@')
    # print(value_2)         #返回的是列表，列表里面的元素是都是字符串
    d={}  #d[key]=value
    for item in value_2:
        item=item.split(":",1)
        # print(item)
        d[item[0]]=item[1]
    L.append(d)
    print(L)