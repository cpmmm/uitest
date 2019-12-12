# -*- coding: utf-8 -*-
'''
@time: 2019/11/9 0009 18:16
@author: chen
@contact: 1171954100@qq.com
@file: demo_py15.py
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
#导入模块
from configparser import ConfigParser
#实例化类
cf=ConfigParser()

#1.读取conf文件：文件路径、编码方式
#相对路径
#绝对路径
cf.read('demo.cfg',encoding='utf-8')

#2.读取所有section列表
secs=cf.sections()
print(secs)

#3.获取某一个sections下面的值，所有options
# print(cf.options(secs[0]))
# print(cf.options("db"))

#4.获取某一个section下面，某一个option具体的值
#所有结果都是字符串
# print(cf.get('db','db_user'))

#获取int类型的值  getint()
# old=cf.get('db','db_port')
# print(type(old))
#
# port=cf.getint('db','db_port')
# print(type(port))

#获取boolean类型的数据 getboolean()
# old=cf.get('excel','res')
# print(type(old))
#
# res=cf.getboolean('excel','res')
# print(type(res))
#
# port=cf.getfloat('db','db_port')
# print(port)
# print(type(port))

sex=cf.get('excel','sex')
print(sex)
print(eval(sex))
print(type(eval(sex)))