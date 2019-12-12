# -*- coding: utf-8 -*-
# @Time:2019/11/6 0006 15:19
# @Author:cp
# @Email:1171954100@qq.com
# @File:homework_0307.py

'''
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
'''1：创建一个名为 Restaurant 的类，其方法 init ()设置两个属性：
 restaurant_name 和 cooking_type。创建一个名为 describe_restaurant()的方法和一个名为 open_restaurant()的方法，
 其中前者打印前述两项信息，而后者打印一条消息， 指出餐馆正在营业。 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，
 再调用前述两个方法。'''
# class Restaurant:
#     def __init__(self,restaurant_name,cooking_type):
#         self.restaurant_name=restaurant_name
#         self.cooking_type=cooking_type
#
#     def describe_restaurant(self):
#         print("饭点名字是{},类型是{}".format(self.restaurant_name,self.cooking_type))
#
#     def open_restaurant(self):
#         print("{}正在营业".format(self.restaurant_name))
#
# Restaurant().restaurant_name("汉丽轩","烧烤")
# Restaurant().cooking_type("烧烤")

'''2:建一个名为 User 的类，其中包含属性 first_name 和 last_name，还有用户简介通常会存储的其他几个属性。
在类 User 中定义一个名为 describe_user()的方法，它打印用户信息摘要；再定义一个名为 greet_user()的方法，
它向用户发出个性化的问候。'''

class User:
    #属性
    first_name="陈"
    last_name="鹏"

    def describe_user(self):
        print("姓名{}{}".format(self.first_name,self.last_name))

    def greet_user(self,name,content='今天也要加油啊!'):      #位置参数   默认参数
        print("{},{}".format(name,content))

#只有在当前文件执行程序的时候下面的代码才会执行
#如果从别的文件里调用这个文件时，下面的代码不执行
#专业属于来说叫主方法，入口
#入口是当前文件

if __name__=='__main__':    #快捷方式，输入main敲回车，这一行都可以出来
    t=User()
    t.describe_user()
    t.greet_user("saber","今天你听懂了没有？")           #saber-->name  今天你听懂了没有？-->content
    print("我就试试你是怎么回事")

