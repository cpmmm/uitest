# -*- coding: utf-8 -*-
# @Time:2019/11/5 0005 16:57
# @Author:cp
# @Email:1171954100@qq.com
# @File:girlFriend.py

class GirlFriends:
    '''这是一个女朋友的类，主要是描述女朋友'''
    #属性
    sex='女'
    height=165

    #方法---90%的相似度--函数
    @staticmethod   #如果有这样一个方法  它跟类里面的属性  函数  没有任何关联的时候 用不到他们
    def coding(language='python'):
        print('会写{},并且写的66的'.format(language))

    def cooking(self,*args):
        dish_name=''          #初始值，空字符串
        for item in args:     #遍历args这个元组
            dish_name+=item   #遍历之后每个都加到dish_name这个字符串上去
            dish_name+='、'   #每个选项之间用、隔开
        print('会做饭，而且很擅长做{}'.format(dish_name))

    @classmethod
    def swimming(cls):    #调用这个方法的时候  会把类作为参数传进来-----》cls类方法的特征
        print("喜欢游泳")

    def print_self(self):       #对象方法，只能对象来调用
        print('self:',self)

#self---调用这个方法的对象本身
#在类外面，类里面的属性和方法，谁可以调用--->对象可以调用类的属性和类的方法
# x=GirlFriends()
# # x.print_self()
# res=x.print_self()
# # print('x:',x)
# print('x:',res)

# x=GirlFriends()
# res=x.print_self('chenpeng')
# print('cp',res)

#对象方法：必须是由对象来进行调用
#类方法：类可以调用  对象可以调用   @classmethod  装饰
# GirlFriends.swimming()
# GirlFriends().swimming()


#静态方法：staticmethod  装饰
GirlFriends.coding()  #类调用
GirlFriends().coding()  #对象调用


#为什么会有对象方法，类方法，静态方法？我什么时候写什么类型的方法呢？
#什么时候用？他们有什么区别呢？