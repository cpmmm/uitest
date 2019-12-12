# -*- coding: utf-8 -*-
'''
@time: 2019/12/5 0005 19:16
@author: chen
@contact: 1171954100@qq.com
@file: study_re.py
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
import re          #解析正则表达式，相当于查找
from API_6.common.config import config

data = '{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'

#原本字符，元字符
# p = "#.*?#"
p = "#(.*?)#"      #正则表达式

# m=re.search(p,data)    #从任意位置开始找，找到第一个就返回  match object，如果没有返回None
# print(m.group())       #返回表达式和组里面的内容    #normal_user#
# print(m.group(1))      #只返回组里面的内容         normal_user
#
# g=m.group(1)
# v=config.get('data',g)
# print(v)
#
# data_new=re.sub(p,v,data,count=1)      #正则，替换的，原来的,count查找替换的次数   sub()查找替换
# print(data_new)
# ms=re.findall(p,data)   #查找全部，返回列表
# print(ms)


#如果要匹配多次，替换多次，使用循环来解决
while re.search(p,data):
    print("替换前的data",data)
    m = re.search(p,data)
    g = m.group(1)
    v=config.get('data',g)
    print(v)

    #记得把替换后的内容用data接收
    data = re.sub(p,v,data,count=1)
    print("替换后的data",data)
print("最后替换后的data",data)