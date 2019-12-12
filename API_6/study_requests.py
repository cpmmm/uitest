# -*- coding: utf-8 -*-
'''
@time: 2019/11/27 0027 10:15
@author: chen
@contact: 1171954100@qq.com
@file: study_requests.py
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

'''
1.构造请求：请求方式，请求地址，请求参数
2.发起请求
3.返回响应
4.判断响应码，响应体
'''

#注册请求
# params={'mobilephone':'15810447878','pwd':'123456'}
# resp=requests.get('http://test.lemonban.com/futureloan/mvc/api/member/register',
#              params=params)      #resp 是一个Response对象
# print('响应码是:',resp.status_code)
# print('响应文本是:',resp.text)
# print('响应头是:',resp.headers)
# print('响应cookies是:',resp.cookies)
# print(resp.request._cookies)


#登录接口
data={'mobilephone':'15810447878','pwd':'123456'}
resp=requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login',
                   data=data)
print('响应码是:',resp.status_code)
print('响应文本是:',resp.text)
print('响应cookies是:',resp.cookies)
print('请求cookies是:',resp.request._cookies)

#充值接口
data={'mobilephone':'15810447878','amount':'1000'}
resp=requests.post('http://test.lemonban.com/futureloan/mvc/api/member/recharge',
                   data=data,
                   cookies=resp.cookies)
print('响应码是:',resp.status_code)
print('响应文本是:',resp.text)
print('响应cookies是:',resp.cookies)
print('请求cookies是:',resp.request._cookies)




