# -*- coding: utf-8 -*-
'''
@time: 2019/12/1 0001 17:37
@author: chen
@contact: 1171954100@qq.com
@file: config.py
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
import configparser
from API_4.common import contants

class ReadConfig:
    '''
    完成配置文件的读取
    '''
    def __init__(self):
        self.config=configparser.ConfigParser()       #先实例化
        self.config.read(contants.global_file)        #先加载global
        switch=self.config.getboolean('switch','on')         #根据section name和option name取值

        if switch:  #开关打开，使用online.conf的配置
            self.config.read(contants.online_file)
        else:       #开关关闭，使用test.conf的配置
            self.config.read(contants.test_file)


    def get(self,section,option):
        return self.config.get(section,option)

config=ReadConfig()

# if __name__ == '__main__':
#     config = ReadConfig()
#     print(config.get('api','pre_url'))
