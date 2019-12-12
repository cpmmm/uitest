# -*- coding: utf-8 -*-
'''
@time: 2019/11/7 0007 14:07
@author: chen
@contact: 1171954100@qq.com
@file: learn_requests.py
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
#requests
#pip install requests  可以使用国内源，详情请看有道云笔记
#作用是什么？        #f发送http请求，get/post
#为什么要学习它       http协议的接口

#request：客户端---服务器的一个请求，包含请求头，请求方法，请求地址，请求参数，http协议版本
#response:服务器---客户端的一个请求的响应，包含：响应头，响应报文，状态码

#常见状态码：200请求成功
#404 网页地址不存在（page not found）url地址错误或找不到
#500 服务器错误  #502网关错误
#304 静态资源png jpeg gif css js 在本地有缓存，并且服务器上的版本未做更改
#docs.python-requests.org/zh_CN/latest/
#www.lemfix.com/topics/198

import requests
url='http://www.lemfix.com/topics/198'        #请求地址

#发送一个get请求
# resp=requests.get(url)   #响应结果的消息实体    包含：响应头，响应报文，状态码
# print(resp.headers)      #响应头
# print(resp.text)         #响应报文
# print(resp.status_code)  #状态码

#发送一个post请求
resp=requests.post(url)
print(resp.headers)      #响应头
print(resp.text)         #响应报文
print(resp.status_code)  #状态码              #404，这个网址不支持post请求

#作业安排
#写一个类，里面有一个函数http_request 能够完成get请求或post请求，要求有返回值
#每个请求要求有请求参数

