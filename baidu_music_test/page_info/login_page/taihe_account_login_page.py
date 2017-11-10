from selenium.webdriver.common.by import By
from baidu_music_test.page_info.page_base import page_base
from baidu_music_test.utils import log_utils

__author__ = '刘子恒'

#此页面为在太合手机号登录页点击账号密码登录后，进入的页面。太合账号密码登录页

class taihe_account_login_page(page_base):
        account_input_bar_xpath="//android.webkit.WebView/android.view.View[4]/android.widget.EditText"        #账号栏
        password_input_bar_xpath="//android.webkit.WebView/android.view.View[5]/android.widget.EditText"       #密码栏
        login_button_xpath="//android.webkit.WebView/android.view.View[6]/android.widget.Button"               #登录按钮
        account_login_log_xpath="//android.view.View[@content-desc=\"太合账号登录\"]"             #账号登录文字栏logo 可用来验证有没有在此页面

        def input_account(self,account=''):
            """功能：
                    输入账号
                参数：
                    account：账号"""
            self.find_element_by_mode_send_keys(By.XPATH,self.account_input_bar_xpath,account)

        def input_password(self,password=''):
            """功能：
                    输入密码
                参数：
                    password：密码"""
            self.find_element_by_mode_send_keys(By.XPATH,self.password_input_bar_xpath,password)

        def click_login_button(self):
            """功能：
                    点击登录按钮
                返回值：
                    1：点击失败"""
            if self.find_element_by_mode_click(By.XPATH,self.login_button_xpath) == 0:
                log_utils.F_ERROR('点击失败')
                return 0






