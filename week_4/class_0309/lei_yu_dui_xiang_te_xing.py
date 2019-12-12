# -*- coding: utf-8 -*-
# @Time:2019/11/6 0006 22:15
# @Author:cp
# @Email:1171954100@qq.com
# @File:lei_yu_dui_xiang_te_xing.py

#继承 拓展  重写
#接着上次的写，新一代手机新出了支付功能
#对象=类名()

from week_4.class_0309.lei_yu_dui_xiang import Phone
class Phone_1(Phone):        #括号里Phone是父类，Phone_1是子类

    def __init__(self):         #如果子类有自己的初始化，就不用继续使用父类
        pass

    def phone_info(self):    #Overrides method in Phone  父类里面有，子类重新写
        #生效范围  在这个子类里面
        print("这是一款新的智能手机")
        self.message('13716424686')

    def pay(self):   #支付功能
        #如果子类里面有父类没有的方法，那么子类的操作叫做拓展
        print('可以支付')

#父类的就是子类的，子类的还是子类的
#继承的作用，子类可以拥有父类里面的所有属性、所有方法，包含初始化方法，记得传参
if __name__ == '__main__':   #导入模块，文件对象  路径操作的时候都讲过
    # Phone_1.call('13269186735')

    # #继承了父类的初始化，需要传参
    # # Phone_1.pay()      这个是错误的
    # Phone_1('red','2300','vivo','5.5').pay()      #这个是对的

    t=Phone_1()
    t.call('13269186735')
    t.pay()
    t.phone_info()

