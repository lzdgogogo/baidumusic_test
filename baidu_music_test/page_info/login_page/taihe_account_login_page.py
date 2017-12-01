from selenium.webdriver.common.by import By
from baidu_music_test.utils import log_utils
from baidu_music_test.utils.base_utils import base_utils
# -*- coding:utf-8 -*-

#此页面为在太合手机号登录页点击账号密码登录后，进入的页面。太合账号密码登录页

class taihe_account_login_page(base_utils):
        def __init__(self):
            super().__init__()

        account_input_bar_xpath="//android.webkit.WebView/android.view.View[4]/android.widget.EditText"        #账号栏
        password_input_bar_xpath="//android.webkit.WebView/android.view.View[5]/android.widget.EditText"       #密码栏
        login_button_xpath="//android.webkit.WebView/android.view.View[6]/android.widget.Button"               #登录按钮
        account_login_log_xpath="//android.view.View[@content-desc=\"太合账号登录\"]"             #账号登录文字栏logo 可用来验证有没有在此页面

        def input_account(self,account=''):
            """功能：
                    输入账号
                参数：
                    account：账号"""
            self.find_element_and_action(By.XPATH,self.account_input_bar_xpath,self.action.send_keys,'输入',account)

        def input_password(self,password=''):
            """功能：
                    输入密码
                参数：
                    password：密码"""
            self.find_element_and_action(By.XPATH,self.password_input_bar_xpath,self.action.send_keys,'输入',password)

        def click_login_button(self):
            """功能：
                    点击登录按钮
                返回值：
                    1：点击失败"""
            if not self.find_element_and_action(By.XPATH,self.login_button_xpath,self.action.click,'登录按钮') == 0:
                log_utils.F_ERROR('点击失败')
                return 1






