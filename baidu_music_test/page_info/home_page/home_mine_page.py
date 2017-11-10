from selenium.webdriver.common.by import By
from baidu_music_test.page_info.home_page.home_page import home_page
from baidu_music_test.utils import log_utils

__author__ = '刘子恒'

#进入首页后点击我的页后，进入的页面，我的页

class home_mine_page(home_page):
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
        play_history_id='com.ting.mp3.android:id/container_playhistory'      #最近播放
        down_load_music_id='com.ting.mp3.android:id/container_downloadmusic' #缓存管理

        def click_unlogin_container(self):
            """功能：
                    点击非登录的头像，进入太合登录页"""
            if self.find_element_by_mode_click(By.ID,self.unlogin_container_id) == 0:
                log_utils.F_ERROR('点击失败')

        def is_login(self):
            """功能：
                    判断是否在登录态
                返回值：
                    1：在登录态
                    0：在非登陆态"""
            try:
                if self.find_element_by_mode_is_displayed(By.ID,self.unlogin_container_id) == 1:
                    return 0
            except:
                if  self.find_element_by_mode_is_displayed(By.ID,self.login_user_img_id) == 1:
                    return 1








