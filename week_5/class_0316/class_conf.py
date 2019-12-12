# -*- coding: utf-8 -*-
'''
@time: 2019/11/9 0009 21:45
@author: chen
@contact: 1171954100@qq.com
@file: read_config.py
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
#读取配置文件
#读取想要的数据：sections?options?字符串？整数？等等
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
    mf=myConfig('demo.cfg')
    res=mf.get_stringValue('db','db_name')
    print(res)

    print(mf.get_sections())
    print(mf.get_options('db'))

#总结：
#1.为什么要用配置文件？接口自动化-配置数据库参数/配置用例的运行模式/服务器地址
#2.配置文件的表达、文件格式：.cfg/.conf
#编写格式：section\option\value   section-区域/块  格式：[section名字]
#在section之下，option=value
#可以有多个section:换行区分

#3.读取配置数据，用的模块：configparser的ConfigParser类
   #1）实例化ConfigParser类，cf=ConfigParser()
   #2）加载配置文件：cf.read(文件名称，编码方式)
   #3）获取配置数据：获取sections：cf.sections()
                 #获取options：cf.options()
                 #获取value：str/int/boolean/float
                        #get(section,option)
                        #getint(section,option)
                        #getboolean(section,option)
                        #getfloat(section,option)

    #初始化---整个类当中，公用的属性赋值
    #各种功能：先把功能函数列出来，再去填充内容