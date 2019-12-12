# -*- coding: utf-8 -*-
# @Time:2019/11/5 0005 16:23
# @Author:cp
# @Email:1171954100@qq.com
# @File:lei_yu_dui_xiang.py

#继承，封装，重写，多态---》语言特性  提高代码复用性
#类的语法
#class 类名:
#    '''类的解释文档'''
      #1）类的方法:功能
      #2）类的属性:特征

#类名的规范：标识符  数字，字母，下划线组成，不能以数字开头  函数名，变量名，模块名都是标识符
#不能用关键字命名，驼峰命名

class GirlFriends:
    '''这是一个女朋友们的类，主要是描述女朋友'''
    #属性
    sex='女'
    height=165

    #方法---90%的相似度--函数
    def coding(self,language):
        print('会写{},并且写的66的'.format(language))

    def cooking(self,*args):
        dish_name=''          #初始值，空字符串
        for item in args:     #遍历args这个元组
            dish_name+=item   #遍历之后每个都加到dish_name这个字符串上去
            dish_name+='、'   #每个选项之间用、隔开
        print('会做饭，而且很擅长做{}'.format(dish_name.strip(dish_name[-1])))
        print('会做饭，而且很擅长做{}'.format(dish_name))

    def swimming(self):
        return "喜欢游泳"

#万物皆对象，对象都是属于某个类的--->类可以产生对象

#创建对象：类名()
t=GirlFriends()    #对象
#对象具有类的所有属性和方法   调用
#对象.属性   对象.方法
print(t.sex)
print(t.height)
t.coding('python')
t.cooking("糖醋鱼",'红烧肉')
res=t.swimming()           #有返回值，有return，所以用res接收起来
print(res)

