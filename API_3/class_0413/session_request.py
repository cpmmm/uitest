# -*- coding: utf-8 -*-
'''
@time: 2019/11/28 0028 9:46
@author: chen
@contact: 1171954100@qq.com
@file: session_request.py
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

session=requests.sessions.Session()  #仿照post里的request方法进行实例化

#注册
params={'mobilephone': '15810447878', 'pwd': '123456'}
resp=session.request('get',
                     'http://test.lemonban.com/futureloan/mvc/api/member/register',
                     params=params)
print(resp.status_code)
print(resp.text)
print(resp.cookies)

#登录
resp=session.request('post',
                url='http://test.lemonban.com/futureloan/mvc/api/member/login',
                data=params)
print(resp.status_code)
print(resp.text)
print(resp.cookies)

#充值
params={'mobilephone':'15810447878','amount':'1000'}
resp=session.request('post',
                url='http://test.lemonban.com/futureloan/mvc/api/member/recharge',
                data=params)
print(resp.status_code)
print(resp.text)
print(resp.request._cookies)

session.close()  #session关闭

