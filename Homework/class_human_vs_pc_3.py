# -*- coding: utf-8 -*-
'''
@time: 2019/11/13 0013 10:41
@author: chen
@contact: 1171954100@qq.com
@file: class_human_vs_pc_3.py
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

    def __init__(self):   #这个初始化下面的变量写成类属性也行
        self.role_dict = {'1': '曹操', '2': '张飞', '3': '刘备'}
        self.fist_dict = {'1': '剪刀', '2': '石头', '3': '布'}


    #选择角色
    def select_role(self):
        role_num = input('请选择角色，{}'.format(self.role_dict))
        # global role_name
        self.role_name = self.role_dict['{}'.format(role_num)]
        print('您选择的是：',self.role_name)
        # return role_name

    #角色出拳
    def role_fist(self):
        global human_fist_num  #角色出拳下面用到了，所以设置成全局
        human_fist_num=input("请出拳,{}".format(self.fist_dict)) #提示用户选择
        human_fist_value=self.fist_dict[human_fist_num]
        print('{}出的是：'.format(self.role_name),human_fist_value)  #打印出来

    #电脑出拳
    def pc_fist(self):
        global pc_fist_num
        pc_fist_num = random.randint(1,3)   #random函数，电脑随机出拳
        pc_fist_value=self.fist_dict['{}'.format(pc_fist_num)]
        print('pc出的是：',pc_fist_value)   #打印电脑出的是什么

    #对战
    def vs(self):   #这块没什么解释的
        if int(human_fist_num) - int(pc_fist_num) in [-2, 1]:
            print("{}win".format(self.role_name))
            self.human_win += 1
        elif int(human_fist_num) - int(pc_fist_num) in [-1, 2]:
            print("pc win")
            self.pc_win += 1
        else:
            print("双方平局")
            self.ping += 1

    #是否继续
    def play_game(self):
        self.select_role()
        while 1:
            self.role_fist()
            self.pc_fist()
            self.vs()
            while 1:
                iscontinue = input('是否继续？按y继续，按n退出')
                if iscontinue not in ('y', 'n'):
                    print('输入错误，请重新输入！')
                    continue
                else:
                    break
            if iscontinue == 'y':
                print('游戏继续！')
                continue
            elif iscontinue == 'n':
                print('游戏结束！')
                print('{}胜{}局   电脑胜{}局   平{}局'.format(self.role_name, self.human_win, self.pc_win, self.ping))
                break



if __name__ == '__main__':
    pk=pK()
    pk.play_game()