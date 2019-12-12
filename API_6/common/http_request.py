# -*- coding: utf-8 -*-
'''
@time: 2019/11/27 0027 18:30
@author: chen
@contact: 1171954100@qq.com
@file: http_request.py
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
from API_6.common.config import *
class HTTPRequest:
    '''
    使用这个类的request方法去完成不同的HTTP请求，并且返回响应结果

    '''

    def request(self,method,url,data,json=None,cookies=None):   #params or data
        method=method.upper()   #转换成大写

        if type(data) == str:
            data=eval(data)

        if method == 'GET':
            resp=requests.get(config.get('api','pre_url')+url,params=data,cookies=cookies)
        elif method == 'POST':
            if json:   #如果json是None，就直接走else语句
                resp=requests.post(config.get('api','pre_url')+url,json=json,cookies=cookies)
            else:
                resp=requests.post(config.get('api','pre_url')+url,data=data,cookies=cookies)
        else:
            print('UN-support method')

        return resp



if __name__ == '__main__':
    data = {'mobilephone': '15810447878', 'pwd': '123456'}
    http_request=HTTPRequest()

    # #调用注册接口，似乎有点小问题
    resp=http_request.request('GET',
                              'http://test.lemonban.com/futureloan/mvc/api/member/register',
                              data=data)
    print(resp.status_code)
    print(resp.text)
    print(resp.cookies)  # 这个是响应cookies

    #调用登录接口
    resp=http_request.request('POST',
                               'http://test.lemonban.com/futureloan/mvc/api/member/login',
                               data=data)
    print(resp.status_code)
    print(resp.text)
    print(resp.cookies)           #这个是响应cookies

    #调用充值接口
    data={'mobilephone':'15810447878','amount':'1000'}
    resp=http_request.request('POST',
                              'http://test.lemonban.com/futureloan/mvc/api/member/recharge',
                              data=data,
                              cookies=resp.cookies)
    print(resp.status_code)
    print(resp.text)
    print(resp.request._cookies)     #这个是请求cookies