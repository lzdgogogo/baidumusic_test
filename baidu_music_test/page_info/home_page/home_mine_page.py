from selenium.webdriver.common.by import By
from baidu_music_test.page_info.home_page.home_page import home_page
from baidu_music_test.utils import log_utils
from baidu_music_test.utils.base_utils import base_utils
# -*- coding:utf-8 -*-

#进入首页后点击我的页后，进入的页面，我的页

class home_mine_page(home_page):
        def __init__(self):
            super().__init__()

        #上边栏
        skin_button_id='com.ting.mp3.android:id/skin'                        #皮肤
        message_button_id='com.ting.mp3.android:id/message'                  #信息
        setting_button_id='com.ting.mp3.android:id/Setting_btn'              #设置

        #注意：用户信息栏  在登录态和非登录态会有区别
        #登录态
        login_user_img_id='com.ting.mp3.android:id/user_img'                 #用户头像
        login_user_name_id='com.ting.mp3.android:id/loginName'               #用户名
        #非登录态
        unlogin_user_img_id='com.ting.mp3.android:id/user_img_unlogin'       #非登录态用户头像框
        unlogin_container_id='com.ting.mp3.android:id/container_unlogin'     #用户非登录布局（点击这里可以进入登录页面）

        #离线缓存、最近播放、缓存管理
        local_music_id='com.ting.mp3.android:id/container_local_music'       #离线缓存
        play_history_id='com.ting.mp3.android:id/img_playhistory'      #最近播放
        download_music_id='com.ting.mp3.android:id/img_downloadmusic' #缓存管理

        def click_play_history_button(self):
            """点击最近播放"""
            if not self.find_element_and_action(By.ID,self.play_history_id,self.action.click,'最近播放') == 0:
                log_utils.F_ERROR('点击失败')

        def click_unlogin_container(self):
            """功能：
                    点击非登录的头像，进入太合登录页"""
            if not self.find_element_and_action(By.ID,self.unlogin_container_id,self.action.click,'头像') == 0:
                log_utils.F_ERROR('点击失败')

        def is_login(self):
            """功能：
                    判断是否在登录态
                返回值：
                    1：在登录态
                    0：在非登陆态"""

            if self.find_element_and_action(By.ID,self.unlogin_container_id,self.action.is_displayed,'非登录态布局') == 0:
                return 0

            elif  self.find_element_and_action(By.ID,self.login_user_img_id,self.action.is_displayed,'用户名') == 0:
                return 1








