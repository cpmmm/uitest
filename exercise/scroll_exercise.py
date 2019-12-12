# -*- coding: utf-8 -*-
'''
@time: 2019/11/16 0016 16:58
@author: chen
@contact: 1171954100@qq.com
@file: scroll_exercise.py
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

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By





from  selenium.webdriver.common.action_chains import ActionChains


from selenium.webdriver.common.keys import Keys    #键盘操作

driver = webdriver.Chrome()   #启动chrome driver
driver.get('http://www.baidu.com')   #打开浏览器，访问网站
driver.maximize_window()

locator = (By.ID,'kw')  #元素定位，(方式，值)
WebDriverWait(driver,30,1).until(EC.visibility_of_element_located(locator))  #等待元素可见 WebDriverWait(driver,30,1) 驱动，等待时长上限，轮巡频率(每X秒查询一次)
driver.find_element(*locator).send_keys('柠檬班',Keys.ENTER)
# time.sleep(3)

locator = (By.XPATH,'''//div[text()="相关搜索"]''')
WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))
ele = driver.find_element(*locator)
driver.execute_script("arguments[0].scrollIntoView(false);",ele)

# arguments[0].scrollIntoView(); 页面顶端
# arguments[0].scrollIntoView(false); 页面底端




time.sleep(3)
driver.quit()