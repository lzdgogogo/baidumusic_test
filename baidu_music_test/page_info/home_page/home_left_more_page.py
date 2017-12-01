from selenium.webdriver.common.by import By
from baidu_music_test.utils import log_utils
from baidu_music_test.utils.base_utils import base_utils
# -*- coding:utf-8 -*-
#此页面为，点击左上角更多按钮，弹出的左侧更多窄页面

class home_left_more_page(base_utils):
        def __init__(self):
            super().__init__()

        user_img_id = 'com.ting.mp3.android:id/user_img'                        #用户头像栏（登录、非登录id一致）

        go_login_button_id = 'com.ting.mp3.android:id/go_login'                 #在非登陆态的立即登录
        user_name_text_id = 'com.ting.mp3.android:id/user_name'                 #登陆后的用户名栏

        setting_container_id = 'com.ting.mp3.android:id/setting_container'      #设定按钮容（通过点击这个可以进入设置页面）

        def click_setting_container(self):
            """功能：
                    点击设置进入设置页面
                返回值：
                    0：点击失败"""
            if not self.find_element_and_action(By.ID,self.setting_container_id,self.action.click,'设置') == 0:
                log_utils.F_ERROR('点击失败')
                return 0

        def check_is_login_in_more_page(self):
            """功能：
                    判断是否在登录态
                返回值：
                    1：在登录态
                    0：没有在登录态"""
            log_utils.C_STEP('判断是否在登录态开始')
            if self.find_element_and_action(By.ID,self.user_name_text_id,self.action.is_displayed,'用户名') == 0:
                return 1
            elif self.find_element_and_action(By.ID,self.go_login_button_id,self.action.is_displayed,'去登陆按钮') == 0:
                return 0


        def click_login_button_in_more_page(self):
            """功能：
                    点击立即登录按钮
                返回值：
                    1：点击失败"""
            if not self.find_element_and_action(By.ID,self.go_login_button_id,self.action.click,'立即登录按钮') == 0:
                log_utils.F_ERROR('点击失败')
                return 1









