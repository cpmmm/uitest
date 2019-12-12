# -*- coding: utf-8 -*-
'''
@time: 2019/12/2 0002 18:36
@author: chen
@contact: 1171954100@qq.com
@file: study_pymysql.py
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
import pymysql

#1.建立连接：数据库的连接信息
host = "test.lemonban.com"
user = "test"
password = "test"
port = 3306

mysql = pymysql.connect(host=host,user=user,password=password,port=port)   #charset有问题

#2.新建一个查询页面
cursor = mysql.cursor()

#3.编写sql
sql = 'select max(mobilephone) from future.member'
# sql = 'select * from future.loan limit 10'

#4.执行mysql
cursor.execute(sql)

#5.查看结果,有两种方法
#第一种方法，获取查询结果集里面的最近的一条数据返回
result= cursor.fetchone()
# print(type(result),result)
print(type(result),result[0])

#第二种方法，获取查询结果集里面的全部数据返回
# result=cursor.fetchall()
# print(type(result),result)

#6.关闭查询
cursor.close()

#7.关闭数据库连接
mysql.close()