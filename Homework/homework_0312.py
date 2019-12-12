# -*- coding: utf-8 -*-
'''
@time: 2019/11/7 0007 15:46
@author: chen
@contact: 1171954100@qq.com
@file: homework_0312.py
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

'''写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值 
每个请求要求有请求参数 
登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login 
请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码 '''
import requests
class HttpRequest:
    #初始化咋写？？？？？？
    def http_request(self,method,url,param):
        '''完成http的get请求或post请求
        method 请求方法  可以是get or post
        url 请求地址
        param 请求参数，字典的格式'''


        if method.lower()=='get':
            try:
        #发送一个get请求：如果请求有参数的话  就要以字典的形式传递过去
                resp=requests.get(url,params=param)
                print('响应报文',resp.text)
            except Exception as e:
                print("get请求出错:{}".format(e))

        elif method.lower()=='post':
        #发送一个post请求
            try:
                resp=requests.post(url,data=param)
                print('响应报文',resp.text)
            except Exception as e:
                print("post请求出错:{}".format(e))
        return resp

if __name__ == '__main__':          #3月2日课程
    url = 'http://192.168.30.128:8080/futureloan/mvc/api/member/login'
    param = {'mobile': '15811101234', 'pwd': 'lemon123456'}
    resp=HttpRequest().http_request('get',login_url,param)   #login_url   or  url?
    print(resp.status_code)  # 状态码

