# -*- coding: utf-8 -*-
# @Time:2019/10/28 0028 17:31
# @Author:cp
# @Email:1171954100@qq.com
# @File:format_print.py

#format_print  格式化输出
name='小明'  #str
age=22   #int str
sex=0 #0是男生 1是女生
salary='9000'   #str float  int
hobby='游泳'    #str
height=170.77  #float
#字符串之间使用+进行拼接，只针对同类型的数据
#可以强制转换str(数字)---->强制转换成字符串
# print('作文中的主角名字是：'+ name + '，他的爱好是'+hobby + ',他今年'+str(age)+'岁')

#第一种格式化输出  %s  %d   %f  占坑，%.2f保留两位小数，%s是万能的，啥都可以接
#数字类型可以用%d %f %s  其他类型必须用%s
print('作文中的主角名字是%s,他的爱好是%s,他今年%d岁,他的身高%.2f'%(name,hobby,age,height))

#第二种格式化输出  {}format   推荐使用
#不标序号，按顺序赋值。
print('作文中的主角名字是{},他的爱好是{},他今年{}岁,他的身高{}'.format(name,hobby,age,height))
#标了序号，按序号赋值，是按照后面顺序的索引值赋值
print('作文中的主角名字是{0},他的爱好是{1},他今年{2}岁,他的身高{3}'.format(name,hobby,age,height))

#三引号
print('''-----student's info----
    作文中的主角名字是{}
    他的爱好是{}
    他今年{}岁
    他的身高{}'''.format(name,hobby,age,height))