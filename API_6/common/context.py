# -*- coding: utf-8 -*-
'''
@time: 2019/12/5 0005 22:43
@author: chen
@contact: 1171954100@qq.com
@file: context.py
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
import re
from API_6.common.config import config

def replace(data):
    p = "#(.*?)#"  # 正则表达式

    while re.search(p, data):
        print("替换前的data", data)
        m = re.search(p, data)
        g = m.group(1)               #拿到参数化的key
        v = config.get('data', g)    #根据key取配置文件里面的值
        print(v)

        # 记得把替换后的内容用data接收
        data = re.sub(p, v, data, count=1)
    #     print("替换后的data", data)
    # print("最后替换后的data", data)

    return data