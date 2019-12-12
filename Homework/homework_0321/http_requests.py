# -*- coding: utf-8 -*-
'''
@time: 2019/11/15 0015 10:54
@author: chen
@contact: 1171954100@qq.com
@file: homework_0321.py
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
'''1：作业安排： 
写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值 
每个请求要求有请求参数 
登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login 
请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码 '''


#   http://192.168.30.128:8080/futureloan/mvc/api/member/login
import requests
class HttpReq:
    #get请求或post请求
    def http_requests(self,login_url,method,param):
        if method.lower()=='get':
            return requests.get(login_url,params=param)
        elif method.lower()=='post':
            return requests.post(login_url,data=param)


if __name__ == '__main__':
    t=HttpReq()
    login_url='http://192.168.30.128:8080/futureloan/mvc/api/member/login'
    param = {'mobilephone': '15810901234', 'pwd': '123456'}
    res=t.http_requests(login_url,'get',param).json()
    print(res)
    print(type(res))

