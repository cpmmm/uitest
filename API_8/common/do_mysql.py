# -*- coding: utf-8 -*-
'''
@time: 2019/12/3 0003 10:28
@author: chen
@contact: 1171954100@qq.com
@file: do_mysql.py
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

class DoMysql:
    '''
    完成与mysql数据库的一个交互
    '''

    def __init__(self):
        host = "test.lemonban.com"
        user = "test"
        password = "test"
        port = 3306

        #创建连接
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port)
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)

    def fetch_one(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()

    def fetch_all(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()     #关闭游标
        self.mysql.close()      #关闭数据库连接

if __name__ == '__main__':
    mysql=DoMysql()
    result=mysql.fetch_one('select max(mobilephone) from future.member')
    print(result)
    mysql.close()
