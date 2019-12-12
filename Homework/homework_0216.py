# -*- coding: utf-8 -*-
# @Time:2019/10/29 0029 10:55
# @Author:cp
# @Email:1171954100@qq.com
# @File:homework_0216.py

#利用input函数获取一个日期，日期格式如下所示：20190216
#然后针对这个日期，进行一些处理后，输出2019年2月16日到控制台

time=input("请输入日期")
# print(time)

#然后切片2019年2月16日，在进行格式化
print("{}年{}月{}日".format(time[:4],time[5],time[6:]))
