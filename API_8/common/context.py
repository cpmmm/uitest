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
from API_7.common.config import config
import configparser


class Context:
    loan_id = None

def replace(data):
    p = "#(.*?)#"  # 正则表达式

    while re.search(p, data):
        print("替换前的data", data)
        m = re.search(p, data)
        g = m.group(1)               #拿到参数化的key

        try:
            v = config.get('data', g)    #根据key取配置文件里面的值
        except configparser.NoOptionError as e:    #如果配置文件里面没有的时候，去Context里面取
            if hasattr(Context,g):
                v=getattr(Context,g)
            else:
                print("找不到参数化的值")
                raise e

        print(v)

        # 记得把替换后的内容用data接收
        data = re.sub(p, v, data, count=1)
    #     print("替换后的data", data)
    # print("最后替换后的data", data)

    return data