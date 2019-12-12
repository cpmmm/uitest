# -*- coding: utf-8 -*-
# @Time:2019/11/2 0002 15:05
# @Author:cp
# @Email:1171954100@qq.com
# @File:dao_ru_mo_kuai.py

# name="chen"
# import os  #为什么要导入？因为每个模块之间都是相互独立的

#导入的第一种方式  import 模块名
#除了顶级项目外，一层一层的去定位你要用的模块 具体到模块名  模块不需要加后缀.py

# import week_3.class_0228.add
# week_3.class_0228.add.add_function(3,5)

#导入方式二: import 模块名 as newname   as取个别名
# import week_3.class_0228.add as t
# t.add_function(4,5)

#导入方式三:from...import...          import后面可以具体到模块名以及函数名以及类名
from week_3.class_0228.add import add_function
add_function(5,6)