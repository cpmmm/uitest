# -*- coding: utf-8 -*-
# @Time:2019/11/2 0002 16:44
# @Author:cp
# @Email:1171954100@qq.com
# @File:robot.py

def robot(name,msg):
    print("{}你有一条信息{}".format(name,msg))

if __name__ == '__main__':      #代码执行的主入口
    robot("小明","吃了吗")