# -*- coding: utf-8 -*-
# @Time:2019/11/6 0006 16:10
# @Author:cp
# @Email:1171954100@qq.com
# @File:lei_yu_dui_xiang.py

#手机类
#属性  颜色，价格，品牌，尺寸
#方法  打电话  发短信  看视频  拍照
#对象方法：必须是由对象来进行调用    self对象方法的标志特征，必须要有！！！
#类方法：类可以调用  对象可以调用    @classmethod  cls类方法的特征，必须要有
#静态方法：类可以调用  对象可以调用
class Phone:
    #属性   属性是变量=====>类属性
    # color='red'
    # price=4500
    # brand="华为"   #品牌
    # size='5.5'

    #参数化--魔法方法---初始化方法
    def __init__(self,color,price,brand,size):     #我们是调用这个方法   #对象属性
        self.color=color
        self.price=price
        self.brand=brand
        self.size=size


    #方法
    @classmethod   #将打电话变成一个类方法
    def call(cls,tel_no):
        print('拨号{}，开始打电话'.format(tel_no))

    def message(self,tel_no,content="早上好"):    #对象方法
        print('给{}发短信:{}'.format(tel_no,content))

    # def watch_tv(self,*args):    #  *args  动态参数
    #     app=''
    #     for item in args:
    #         app+=item
    #         app+='、'
    #     print(len(app))
    #     print('可以利用这些app看视频，比如说{}'.format(app))
    def watch_tv(self, *args):  # *args  动态参数  args传进来是个元组
        app = ''
        for item in args:
            app += item
            app += '、'
        print('可以利用这些app看视频，比如说{}'.format(app.strip(app[-1])))
        print(type(app))


    def take_shoot(self):  #拍照
        print('拍照')

    @staticmethod  #静态方法--->工具方法  跟对象，类，没有任何关联  他也不会调用任何类里面的方法或者是属性
    def add(a,b):     #加法
        print(a+b)

    def phone_info(self):
        print('颜色:{}，品牌:{}，价格:{}，尺寸:{}'
              .format(self.color,self.brand,self.price,self.size))

if __name__ == '__main__':
    t=Phone('red','2300','vivo','5.5')     #color,price,brand,size   有初始化方法，创建对象时，有几个参数传几个参数
    t.add(4,5)
    print(t.size)
    print(t.price)
    print(t.brand)
    t.take_shoot()
    t.watch_tv('爱奇艺','优酷','腾讯视频')
    t.message('13716424686','今天也要加油啊')
    t.phone_info()