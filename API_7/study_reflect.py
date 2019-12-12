# -*- coding: utf-8 -*-
'''
@time: 2019/12/7 0007 14:06
@author: chen
@contact: 1171954100@qq.com
@file: study_reflect.py
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
class People:
    number_eye = 2

    def __init__(self,name,age):
        self.name =name
        self.age = age

if __name__ == '__main__':
    p = People('chen',25)
    print(p.number_eye)
    print(People.number_eye)
    print(p.name)

    print("----------------")

    #添加属性
    print(hasattr(People,"number_leg"))        #如果有返回True，没有返回False
    print(hasattr(People,"number_eye"))

    setattr(People,"number_leg",2)
    print(hasattr(People, "number_leg"))

    print("----------------")

    print(People.number_leg)


    setattr(p,"dance",True)
    print(p.dance)

    getattr(People,"number_leg")   #获取类属性
    getattr(p,"dance")             #获取实例属性

    delattr(p,"dance")             #删除
    getattr(p,"dance")             #获取实例属性     删除后在获取会报错

