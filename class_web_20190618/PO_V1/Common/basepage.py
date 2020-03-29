# -*- coding: utf-8 -*-
'''
@time: 2020/1/12 0012 15:29
@author: chen
@contact: 1171954100@qq.com
@file: basepage.py
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
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from class_web_20190618.PO_V1.Common.dir_config import screenshot_dir
import time

from class_web_20190618.PO_V1.Common import logger

#引入日志文件
logger = logger.get_logger(__name__)

class BasePage:

    """
    包含了PageObjects当中，用到所有的selenium底层方法
    还可以包含通用的一些元素操作，如alert，iframe，windows切换。。。
    还可以自己额外封装一些web相关的断言
    实现日志记录，实现失败截图
    """

    # 初始化driver
    def __init__(self, driver):
        self.driver = driver


    # 封装函数

    #等待元素可见
    def wait_eleVisible(self,loc,img_doc="",timeout=30,frequency=0.5):
        logger.info("等待元素 {} 可见".format(loc))      #将logging改成logger
        try:
            #起始等待的时间 datetime
            start = datetime.datetime.now()
            WebDriverWait(self.driver,timeout,frequency).until(EC.visibility_of_element_located(loc))

            #结束等待的时间
            end = datetime.datetime.now()

            logger.info("开始等待时间：{}，结束等待时间：{}，等待时长为：{}"
                         .format(start,end,end-start))
        except:
            #日志
            logger.exception("等待元素可见失败")
            # 截图 - 哪一个用例，哪一个页面，哪一步操作导致的失败 + 当前时间
            self.save_web_screenshot(img_doc)
            raise

    #实现网页截图操作
    def save_web_screenshot(self,img_doc):
        # 截图 - 哪一个用例，哪一个页面，哪一步操作导致的失败 + 当前时间
        # 页面_功能_时间.png
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filepath = "{}_{}.png.".format(img_doc,now)
        try:
            self.driver.save_screenshot(screenshot_dir + "/" + filepath)
            logger.info("网页截图成功，图片存储在:{}".format(screenshot_dir + "/" + filepath))
        except:
            logger.info("网页截屏失败！")
            raise

    #查找一个元素
    def get_element(self,loc,img_doc=""):
        """
        :param loc:元素定位，以元组形式。（定位类型，定位时间）
        :param img_doc:截图的说明。例如：登录页面_输入用户名
        :return:WebElement对象
        """
        logger.info("查找{}中的{}元素".format(img_doc,loc))
        try:
            ele = self.driver.find_element(*loc)
            return ele
        except:
            #日志
            logger.info("查找元素失败")
            #截图
            self.save_web_screenshot(img_doc)
            raise

    def click_element(self,loc,img_doc,timeout=30,frequency=0.5):
        """
        实现了等待元素可见，找元素，然后再去点击元素
        :param loc:元素定位，以元组形式。（定位类型，定位时间）
        :param img_doc:截图的说明。例如：登录页面_输入用户名
        :param timeout:时间
        :param frequency:频率
        :return:
        """
        #1.等待元素可见
        self.wait_eleVisible(loc,img_doc,timeout,frequency)
        #2.找元素
        ele = self.get_element(loc,img_doc)      #改动
        #3.再操作
        logger.info("点击元素{}".format(loc))
        try:
            ele.click()
        except:
            # 日志
            logger.info("点击元素失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    def input_text(self,loc,img_doc,*args):
        #1.等待元素可见
        self.wait_eleVisible(loc,img_doc)
        #2.找元素
        ele = self.get_element(loc,img_doc)        #改动
        #3.再操作
        logger.info("给元素{}输入文本内容：{}".format(loc,args))
        try:
            ele.send_keys(*args)
        except:
            # 日志
            logger.info("元素输入操作失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    #获取元素的属性值
    def get_element_attribute(self,loc,attr_name,img_doc):
        # 1.等待元素可见
        self.wait_eleVisible(loc, img_doc)
        #2.找元素
        ele = self.get_element(loc,img_doc)
        #获取属性
        try:
            attr_value = ele.get_attribute(attr_name)
            logger.info("获取元素{}的属性{}值为：{}".format(loc, attr_name,attr_value))
            return attr_value
        except:
            # 日志
            logger.info("获取元素属性值操作失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    #获取元素文本值
    def get_element_text(self,loc,img_doc):
        # 1.等待元素可见
        self.wait_eleVisible(loc, img_doc)
        # 2.找元素
        ele = self.get_element(loc,img_doc)
        #获取文本值
        try:
            text = ele.text
            logger.info("获取元素{}的文本值为：{}".format(loc,text))
            return text
        except:
            #日志
            logger.info("获取元素文本值操作失败")
            #截图
            self.save_web_screenshot(img_doc)
            raise

    #获取弹出框文本值
    def get_alert_text(self,loc,img_doc,timeout=30,frequency=0.1):
        #1.点击元素，导致弹出框出现
        self.click_element(loc,img_doc)
        #2.等待弹出框出现
        WebDriverWait(self.driver,timeout,frequency).until(EC.alert_is_present())
        #3.切换，并用alert接收
        alert = self.driver.switch_to.alert
        time.sleep(3)
        #获取弹出框文本值
        try:
            text = alert.text
            logger.info("获取弹出框文本值为:{}".format(text))
            return text
            alert.accept()
            time.sleep(2)
        except:
            # 日志
            logger.info("获取弹出框文本值操作失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise


    #另外默认参数frequency=0.1，那么后面的frequency是多少？



