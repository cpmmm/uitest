# -*- coding: utf-8 -*-
'''
@time: 2019/11/7 0007 15:06
@author: chen
@contact: 1171954100@qq.com
@file: learn_requests_2.py
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
import requests
#登录请求地址:http://47.107.168.87:8080/futureloan/mvc/api/member/login
#mobile:18688773467  pwd:123456   登录时需要提供手机号和密码

login_url='http://test.lemonban.com/futureloan/mvc/api/member/login'
param={'mobile':'18688773467','pwd':'123465'}        #get函数里明确写出参数要放在字典里
#发送一个get请求
# resp=requests.get(login_url,params=param)
# print('响应头:',resp.headers)      #响应头
# print('响应报文',resp.text)         #响应报文
# print('状态码',resp.status_code)  #状态码              #404，这个网址不支持post请求


#发送一个post请求
resp=requests.post(login_url,data=param)
print('响应头:',resp.headers)      #响应头
print('响应报文',resp.text)         #响应报文
print('状态码',resp.status_code)  #状态码              #404，这个网址不支持post请求

#作业安排
#写一个类，里面有一个方法  http_request 能够完成get请求或post请求，要求有返回值
#每个请求要求有请求参数

#字典和json对比
d1={'mobile':'18688773467','pwd':'123465','data':None}       #字典  None

d2='{"mobile":"18688773467","pwd":"123465","data":null}'     #json格式的字符串，必须是双引号，null

#把json转成字典
import json
print(json.loads(d2))   #字符串类型的json格式---python的字典格式
