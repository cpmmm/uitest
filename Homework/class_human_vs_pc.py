# -*- coding: utf-8 -*-
'''
@time: 2019/11/12 0012 11:14
@author: chen
@contact: 1171954100@qq.com
@file: class_human_vs_pc.py
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
import random
#写一个类，类里面要有选择角色，角色出拳，电脑出拳，对战，是否继续
class pK:
    pc_win = 0
    human_win = 0
    ping = 0
    role_name=''


    def __init__(self):
        self.role_dict= {'1': '曹操', '2': '张飞', '3': '刘备'}
        self.fist_dict= {'1': '剪刀', '2': '石头', '3': '布'}

    #选择角色
    def select_role(self):
        while True:
            role_num = input('请输入选择的角色：1 曹操 2张飞 3 刘备')
            if role_num not in ('1','2','3'):
                print("输入有误，请重新输入")
                continue
            else:
                break
        self.role_name=self.role_dict[role_num]
        print('您选择的角色是:',self.role_name)

    #角色出拳
    def role_fist(self):
        global human_fist_num
        while True:
            human_fist_num=input("请出拳:1剪刀，2石头，3布")
            if human_fist_num not in ('1','2','3'):
                print("输入有误，请重新输入")
                continue
            else:
                break
        human_fist_value=self.fist_dict[human_fist_num]
        print('角色出拳为:',human_fist_value)

    #电脑出拳
    def pc_fist(self):
        global pc_fist_num
        pc_fist_num=random.randint(1,3)
        # pc_fist_value=self.fist_dict[str(pc_fist_num)]
        pc_fist_value=self.fist_dict['{}'.format(pc_fist_num)]
        print('pc出拳为:',pc_fist_value)

    #对战
    def vs(self):
        if int(human_fist_num) - pc_fist_num in [-2, 1]:
            print("{}win".format(self.role_name))
            self.human_win += 1
        elif int(human_fist_num) - pc_fist_num in [-1, 2]:
            print("pc win")
            self.pc_win += 1
        else:
            print("双方平局")
            self.ping += 1
    #
    #是否继续
    def is_continue(self):
        self.select_role()
        while True:
            self.role_fist()
            self.pc_fist()
            self.vs()
            while True:
                choice=input("是否继续?y继续，n退出")
                if choice not in ('y','n'):
                    print('输入错误，请重新输入！')
                    continue
                else:
                    break
            if choice == 'y':
                print("游戏继续喽！")
                continue
            elif choice == 'n':
                print("游戏结束！")
                print('{}胜{}局，pc胜{}局，平了{}局'.format(self.role_name,self.human_win,self.pc_win,self.ping))
                break

if __name__ == '__main__':
    pk=pK()
    pk.is_continue()

