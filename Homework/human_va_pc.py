# -*- coding: utf-8 -*-
'''
@time: 2019/11/13 0013 14:11
@author: chen
@contact: 1171954100@qq.com
@file: human_va_pc.py
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
#写一个类，类里面要有选择角色，人出拳，电脑随机出拳，对战，是否继续
import random
class pK():
    human_win=0
    pc_win=0
    ping=0
    role_name=''

    def __init__(self):
        '''初始化'''
        self.role_dict={'1':'曹操','2':'刘备','3':'孙权'}
        self.fist_dict={'1':'剪刀','2':'石头','3':'布'}

    #选择角色
    def select_role(self):
        row_num=input("请输入选择的角色，1曹操，2刘备，3孙权")
        self.role_name=self.role_dict['{}'.format(row_num)]
        print('您选择的角色是:{}'.format(self.role_name))

    #角色出拳
    def role_fist(self):
        global human_fist_num
        human_fist_num=input("请出拳，1剪刀，2石头，3布")
        human_fist_value=self.fist_dict['{}'.format(human_fist_num)]
        print("{}出拳为:{}".format(self.role_name,human_fist_value))

    #电脑随机出拳
    def pc_fist(self):
        global pc_fist_num
        pc_fist_num=random.randint(1,3)
        pc_fist_value=self.fist_dict['{}'.format(pc_fist_num)]
        print("pc出拳为:{}".format(pc_fist_value))

    #对战
    def vs(self):
        '''分析
        human win
        human   1---pc   3---   -2
        human   2---pc   1---   1
        human   3---pc   2---   1

        pc  win
        human   1---pc   2---   -1
        human   2---pc   3---   -1
        human   3---pc   1---    2

        ping  一样
        '''
        if int(human_fist_num)-pc_fist_num in [-2,1]:
            print('{}win!'.format(self.role_name))
            self.human_win+=1
        elif int(human_fist_num)-pc_fist_num in [-1,2]:
            print('pc win!')
            self.pc_win+=1
        else:
            print("双方平局!")
            self.ping+=1

    #是否继续
    def is_continue(self):
        self.select_role()
        while True:
            self.role_fist()
            self.pc_fist()
            self.vs()
            while True:
                choice = input("是否继续？y继续，n退出")
                if choice not in ['y','n']:
                    print("输入有误，请重新输入")
                    continue
                else:
                    break
            if choice=='y':
                print("游戏继续！")
                continue
            elif choice =='n':
                print('游戏结束！')
                print("{}赢了{}局，pc赢了{}局，平了{}局".format(self.role_name,self.human_win,self.pc_win,self.ping))
                break


if __name__ == '__main__':
    pk=pK()
    pk.is_continue()