# -*- coding: utf-8 -*-
'''
@time: 2019/12/21 0021 19:16
@author: chen
@contact: 1171954100@qq.com
@file: study_suds.py
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
from suds.client import Client
import suds

#建立一个客户端
#获取短信验证码
url = 'http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl'
client = Client(url)    #实例化
print(client)

data={"client_ip":"127.0.0.1","tmpl_id":1,"mobile":19000000000}
try:
    resp = client.service.sendMCode(data)
    print(type(resp))
    print("返回码是:",resp.retCode)
    print("返回信息是:",resp.retInfo)
except suds.WebFault as e:
    print(e.fault.faultstring)

#注册
url = 'http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl'
data = {"verify_code":296801,"user_id":"霹雳娇娃","channel_id":1,
        "pwd":"123456","mobile":"15878787878","ip":"127.0.0.1"}
client = Client(url)

try:
    resp = client.service.userRegister(data)
    print(type(resp))
    print("返回码是:",resp.retCode)
    print("返回信息是:",resp.retInfo)
except suds.WebFault as e:
    print(e.fault.faultstring)

def ws_request(url,data,method):
    client = Client(url)
    try:
        resp = eval("client.service.{0}({1})".format(method,data))
        msg = resp.retInfo
        print(type(resp))
        print("返回码是:",resp.retCode)
        print("返回信息是:",resp.retInfo)
    except suds.WebFault as e:
        print(e.fault.faultstring)
        msg = e.fault.faultstring

    return msg

url = 'http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl'
data = {"uid":100010710,"true_name":"张三","cre_id":"43041219900101002Z"}
resp = ws_request(url,data,"verifyUserAuth")
print(resp)