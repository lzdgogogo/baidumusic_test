import os
import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys
from baidu_music_test.data import base_data
from baidu_music_test.utils import log_utils
import time

__author__ = '刘子恒'

class base_utils(object):

        TIME=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))

        def __init__(self):
                """功能：
                        初始化driver"""
                desired_caps={}
                desired_caps['platformName']=base_data.PlatformName
                desired_caps['platformVersion']=base_data.PlatformVersion
                desired_caps['deviceName']=base_data.DeviceName
                desired_caps['appPackage']=base_data.AppPackage
                desired_caps['appActivity']=base_data.AppActivity
                self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
                log_utils.C_INFO('测试开始')

        def tear_down(self):
                """功能：
                        关闭APP，driver退出，结束测试"""
                self.driver.close_app()
                self.driver.quit()
                log_utils.C_INFO('测试结束！')

        number=1
        def screenshot(self,des=''):
                """功能：
                        截屏，图片放在一个名为程序开始时间的文件夹里面，每张图片的命名方式为“序号。时间。描述”
                参数：
                        截图描述，为一个字符串"""

                temp_path=os.path.abspath(os.getcwd()+'/screenshot'+'/'+self.TIME)
                if not os.path.isdir(temp_path):        #检查文件夹是否存在
                      os.makedirs(temp_path)
                temp_time = time.strftime('%H-%M-%S',time.localtime(time.time()))
                self.driver.get_screenshot_as_file(temp_path+'/'+'%d'%self.number+'.'+temp_time+'.'+des+'.png')
                self.number += 1

        def wait_element_by_mode(self,t,mode,element='',thing=''):
                """功能：
                        等待某控件出现，等待一段规定的时间，假如没有出现就会报错跳出
                参数：
                        t：设置等待的时间
                        mode：查找模式，例如By,ID,By.XPATH
                        element：等待的控件查找依据，比如id,xpath,必须要跟mode的模式相匹配
                        thing：等待的元素的描述"""
                try:
                        WebDriverWait(self.driver,t).until(expected_conditions.presence_of_element_located((mode,element)))
                except:
                        log_utils.F_ERROR(thing+'超时')
                        self.screenshot('错误截图：'+thing+'等待超时')
                        self.driver.quit()
                        sys.exit(-1)
                log_utils.C_INFO(thing+'成功')

        def reset_app(self):
                """功能：
                        重启APP，并且等待app重启完成"""
                self.driver.close_app()
                self.driver.launch_app()
                self.wait_element_by_mode(base_data.wait_time_long,By.ID,base_data.sign_element_id,'重启App')

        def wait_start_app(self):
                """功能：
                        等待app启动完成"""
                self.wait_element_by_mode(base_data.wait_time_long,By.ID,base_data.sign_element_id,'启动App')

        @staticmethod
        def my_sleep(t=1):
                """功能：
                        程序睡眠t秒"""
                time.sleep(t)

        def get_size(self):
                """功能：
                        获取本机的分辨率，返回值是屏幕的长和宽"""
                x=self.driver.get_window_size()['width']
                y=self.driver.get_window_size()['height']
                return x,y

        def my_swipe(self,direction='',t=500,x=0.5):
                """功能：
                        模仿手指在屏幕上的滑动动作
                参数：
                        direction：方向，有四个选项（up,down,left,right）
                        t：滑动的时间，t越小代表滑的越快，滑的距离越大，但是t不可以过小，想快速滑动最小设置为500，t的单位是毫秒。
                        x：向上下滑动时手指在屏幕的横向位置，向左右滑动时的竖向位置
                        例如x=0.5，手指就在屏幕中间向下滑，x=0.25，就在屏幕四分之一的地方向下滑"""

                size = self.get_size()
                if direction == 'up':
                        x1=int(size[0]*x)
                        y1=int(size[1]*0.75)
                        y2=int(size[1]*0.25)
                        self.driver.swipe(x1,y1,x1,y2,t)
                elif direction == 'down':
                        x1 = int(size[0] * x)
                        y1 = int(size[1] * 0.25)
                        y2 = int(size[1] * 0.75)
                        self.driver.swipe(x1,y1,x1,y2,t)
                elif direction == 'left':
                        x1 = int(size[0] * 0.9)
                        x2 = int(size[0] * 0.1)
                        y1 = int(size[1] * x)
                        self.driver.swipe(x1,y1,x2,y1,t)
                elif direction == 'right':
                        x1 = int(size[0] * 0.1)
                        x2 = int(size[0] * 0.9)
                        y1 = int(size[1] * x)
                        self.driver.swipe(x1,y1,x2,y1,t)
                else:
                        log_utils.F_ERROR('error,please inset right paremater!')
                        sys.exit()

        def is_element_display(self,mode,element='',thing=''):
                """功能：
                        判断控件是否显示在当前页面上
                参数：
                        mode：以哪种方式寻找控件，必须是以下几种:By.ID, By.CLASS_NAME, By.XPATH, By.NAME
                        element：控件的id或者xpath等，要跟前一项对应，
                        thing：描述
                返回值：
                        1：查找的控件显示
                        0：查找的控件不显示
                        -1：查找不到要查找的控件，抛出异常
                例子：
                        self.is_element_display(By.ID,'com.ting.mp3.android:id/day_tv','首页控件')"""
                try:
                        if self.driver.find_element(mode,element).is_displayed():
                                log_utils.C_INFO(thing+'显示')
                                return 1
                        else:
                                log_utils.F_ERROR(thing+'未显示')
                                return 0
                except:
                        log_utils.F_ERROR(thing+'不在当前页面')
                        self.screenshot('错误截图：要查找控件不在当前页面')
                        return -1

        def find_element_and_click(self,mode,element='',thing=''):
                """功能：
                        以某种方式查找控件并且点击，但是保证不会因为找不到控件而跳出
                参数：
                        mode：以哪种方式寻找控件，必须是以下几种:By.ID, By.CLASS_NAME, By.XPATH, By.NAME
                        element：控件的id或者xpath等，要跟前一项对应，
                        thing：描述
                返回值：
                        1：点击成功
                        -1：控件不在当前页面
                例子：
                        if self.find_element_and_click(By.ID,'com.ting.mp3.android:id/day_tv') == -1:   sys.exit()"""

                try:
                        self.driver.find_element(mode,element).click()
                        log_utils.C_INFO('点击'+thing)
                        return 1
                except:
                        log_utils.F_ERROR(thing+'不在当前页面')
                        self.screenshot('错误截图：要点击控件不在当前页面')
                        return -1











