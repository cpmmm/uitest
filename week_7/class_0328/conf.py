# -*- coding: utf-8 -*-
'''
@time: 2019/11/21 0021 15:28
@author: chen
@contact: 1171954100@qq.com
@file: conf.py
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
from configparser import ConfigParser

class myConfig:
    def __init__(self,file_path,encoding='utf-8'):

        # 读取配置文件
        self.cf=ConfigParser()
        self.cf.read(file_path,encoding)

    def get_intValue(self,section,option):
        return self.cf.getint(section,option)

    def get_booleanValue(self,section,option):
        return self.cf.getboolean(section,option)

    def get_stringValue(self,section,option):
        return self.cf.get(section,option)

    def get_floatValue(self,section,option):
        return self.cf.getfloat(section,option)

    def get_sections(self):
        return self.cf.sections()

    def get_options(self,section):
        return self.cf.options(section)

if __name__ == '__main__':
    mf=myConfig('peizhi.cfg')
    res=mf.get_stringValue('email','email_name')
    print(res)

    print(mf.get_sections())
    print(mf.get_options('email'))

