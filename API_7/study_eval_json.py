# -*- coding: utf-8 -*-
'''
@time: 2019/11/29 0029 9:58
@author: chen
@contact: 1171954100@qq.com
@file: study_eval_json.py
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
import json
#正常的json格式   {"key":"value"}
#入参eval(),出参json()
params='{"status":1,"code":"10001","data":null,"msg":"登录成功"}'

# d=eval(params)              #根据python语法做转换，但是python语法中没有null
# print(d['status'])

d1=json.loads(params)
print(type(d1),d1)
print(d1['msg'])


p='{"mobilephone":"15810447878","pwd":None}'       #请求入参
d2=eval(p)
print(d2)