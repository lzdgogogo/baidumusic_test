from selenium.webdriver.common.by import By
from baidu_music_test.page_info.page_base import page_base
from baidu_music_test.utils import log_utils

__author__ = '刘子恒'
#此页面为tpass登录首页，登录方式是手机号和短信验证码登录

class taihe_phonenumber_login_page(page_base):
        go_to_account_login_button_xpath="//android.view.View[@content-desc=\"账号密码登录\"]"     #去账号密码登录页按钮
        go_to_baidu_login_button_xpath="//android.view.View[@content-desc=\"百度账号登录\"]"       #去百度登录页按钮
        go_to_other_login_button_xpath="//android.view.View[@content-desc=\"其他方式登录\"]"       #其他方式登录按钮

        def go_to_account_login_page(self):
                """功能：
                        点击账号密码登录页按钮，去账号密码登录页"""
                if self.find_element_by_mode_click(By.XPATH,self.go_to_account_login_button_xpath) == 0:
                    log_utils.F_ERROR('点击失败')
                    return 0


        def go_to_baidu_login_page(self):
                """功能：
                        点击百度账号登录按钮，去百度登录页"""
                if self.find_element_by_mode_click(By.XPATH,self.go_to_baidu_login_button_xpath) == 0:
                    log_utils.F_ERROR('点击失败')
                    return 0

        def go_to_other_login_page(self):
                """功能：
                        点击其他方式登录按钮"""
                if self.find_element_by_mode_click(By.XPATH,self.go_to_other_login_button_xpath) == 0:
                    log_utils.F_ERROR('点击失败')
                    return 0








