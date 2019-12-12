# -*- coding: utf-8 -*-
'''
@time: 2019/11/28 0028 10:20
@author: chen
@contact: 1171954100@qq.com
@file: http_request2.py
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
from API_4.common.config import config

class HTTPRequest2:
    '''
       使用这个类的request方法去完成不同的HTTP请求，并且返回响应结果

       '''
    def __init__(self):
        #打开一个session
        self.session=requests.sessions.Session()

    def request(self,method,url,data=None,json=None):
        method=method.upper()       #转换成大写
        if type(data) == str:
            data=eval(data)

        #拼接请求的url,再传到url=url的后面的url中
        url=config.get('api','pre_url')+url

        if method =='GET':
            resp =self.session.request(method=method,url=url,params=data)
        elif method =='POST':
            if json:
                resp=self.session.request(method=method,url=url,json=json)
            else:
                resp =self.session.request(method=method,url=url,data=data)
        else:
            resp=None
            print('UN-support method')
        return resp

    #session关闭
    def close(self):
        self.session.close()

if __name__ == '__main__':
    http_request2 = HTTPRequest2()

    data = {'mobilephone': '15810447878', 'pwd': '123456'}

    #注册
    resp2=http_request2.request('get',
                          'http://test.lemonban.com/futureloan/mvc/api/member/register',
                          data=data)
    print(resp2.status_code)
    print(resp2.text)
    print(resp2.cookies)

    #登录
    resp2=http_request2.request('post',
                         'http://test.lemonban.com/futureloan/mvc/api/member/login',
                         data=data)
    print(resp2.status_code)
    print(resp2.text)
    print(resp2.cookies)

    #充值
    data={'mobilephone':'15810447878','amount':'1000'}
    resp2=http_request2.request('post',
                         'http://test.lemonban.com/futureloan/mvc/api/member/recharge',
                         data=data)
    print(resp2.status_code)
    print(resp2.text)
    print(resp2.request._cookies)

    http_request2.close()
