from selenium.webdriver.common.by import By
from baidu_music_test.page_info.home_page.home_page import home_page
from baidu_music_test.page_info.page_base import page_base
from baidu_music_test.utils import log_utils

__author__ = '刘子恒'
#此页面为，点击左上角更多按钮，弹出的左侧更多窄页面

class home_left_more_page(page_base):
        user_img_id = 'com.ting.mp3.android:id/user_img'                        #用户头像栏（登录、非登录id一致）

        go_login_button_id = 'com.ting.mp3.android:id/go_login'                 #在非登陆态的立即登录
        user_name_text_id = 'com.ting.mp3.android:id/user_name'                 #登陆后的用户名栏

        setting_container_id = 'com.ting.mp3.android:id/setting_container'      #设定按钮容（通过点击这个可以进入设置页面）

        def click_setting_container(self):
            """功能：
                    点击设置进入设置页面
                返回值：
                    0：点击失败"""
            if self.find_element_by_mode_click(By.ID,self.setting_container_id) == 0:
                log_utils.F_ERROR('点击失败')
                return 0

        def is_login(self):
            """功能：
                    判断是否在登录态
                返回值：
                    1：在登录态
                    0：没有在登录态"""
            try:
                if self.find_element_by_mode_is_displayed(By.ID,self.user_name_text_id):
                        return 1

            except:
                if self.find_element_by_mode_is_displayed(By.ID,self.go_login_button_id):
                        return 0


        def click_login_button(self):
            """功能：
                    点击立即登录按钮
                返回值：
                    0：点击失败"""
            if self.find_element_by_mode_click(By.ID,self.go_login_button_id) == 0:
                log_utils.F_ERROR('点击失败')
                return 0









