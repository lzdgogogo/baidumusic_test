from selenium.webdriver.common.by import By
import sys
from baidu_music_test.data import base_data
from baidu_music_test.data import account_data
from baidu_music_test.page_info.dialog_page import dialog_page
from baidu_music_test.page_info.setting_page import setting_page
from baidu_music_test.page_info.home_page.home_left_more_page import home_left_more_page
from baidu_music_test.page_info.home_page.home_music_page import home_music_page
from baidu_music_test.page_info.login_page.taihe_account_login_page import taihe_account_login_page
from baidu_music_test.page_info.login_page.taihe_phonenumber_login_page import taihe_phonenumber_login_page
from baidu_music_test.utils import log_utils



__author__ = '刘子恒'

class login_case(home_music_page,home_left_more_page,taihe_phonenumber_login_page,taihe_account_login_page,dialog_page,setting_page):

    def after_login(self):
        """功能：
                登录前的步骤，主页--点击更多按钮--验证是否在登录态--点击登录进入登录页"""
        log_utils.C_INFO('开始登陆')

        self.click_more_button()             #点击更多按钮
        log_utils.C_INFO('查看登录态开始')
        self.my_sleep()
        if self.check_is_login_in_more_page() == 1:
            log_utils.F_ERROR('已经在登录态了！先去退出登录')
            self.screenshot('错误--已经在登录态截图')
            self.reset_app()
            if self.sign_out() == 0:
                log_utils.F_ERROR('登出功能已经失效！无法继续测试！程序退出！')
                self.tear_down()
                sys.exit(-1)
            else:
                log_utils.C_INFO('登出成功！继续测试登录功能！')
                self.reset_app()
                log_utils.C_INFO('开始登陆')
                self.click_more_button()             #点击更多按钮

        self.click_login_button_in_more_page()        #点击立即登录

    def taihe_login(self,mode):
        """功能：
                验证太合登录的主过程：验证是否进入登录页--点击进入账号密码登录页--验证是否进入账号密码登录页--输入账号密码--验证登录态
            参数：
                mode：1--输入正确的账号密码       2--输入错误的密码      3--输入错误的账号
            返回值：
                1：在登录态
                0：不在登录态
            注意：
                太合登录有一个输入错误密码次数达到三次的时候就开始弹出验证码的策略，因此不可以连续多次输入错误的密码"""

        self.wait_element_by_mode(base_data.wait_time_mid,By.XPATH,self.go_to_baidu_login_button_xpath,'进入登录页')
        self.go_to_account_login_page()
        self.wait_element_by_mode(base_data.wait_time_mid,By.XPATH,self.account_login_log_xpath,'进入账号密码登录页')
        if mode == 1:
            self.input_account(account_data.TAIHE_PHONE_NUMBER)         #输入账号密码，点击登录按钮，点击登录后会联网登录，返回首页
            self.input_password(account_data.TAIHE_PASSWORD)
            self.screenshot('输入账号密码截图')
            self.click_login_button()
        elif mode == 2:
            self.input_account(account_data.TAIHE_PHONE_NUMBER)         #输入账号密码，点击登录按钮，点击登录后会联网登录，返回首页
            self.input_password('wrong_password')                       #输入错误的密码
            self.screenshot('输入账号密码截图')
            self.click_login_button()
            log_utils.C_STEP('输入错误的密码，点击登录按钮')                                      #验证错误密码的异常情况的方法是，睡眠几秒，观察是否停留在此页
            self.screenshot('输入错误密码后截图')
            self.my_sleep(5)
            if self.find_element_and_action(By.XPATH,self.login_button_xpath,'is_displayed','账号密码登录页') == 0:
                return 0
            else:
                return 1

        self.wait_element_by_mode(base_data.wait_time_long,By.ID,self.more_button_id,'回到首页')     #验证登录态
        self.click_more_button()
        self.my_sleep()
        log_utils.C_STEP('点击更多按钮，验证登录态')
        self.screenshot('登录态截图')
        if self.check_is_login_in_more_page() == 1:
            log_utils.C_INFO('在登录态')
            return 1
        else:
            log_utils.C_INFO('不在登录态')
            return 0

    def sign_out(self):
        """功能：
                登出的主过程：点击更多按钮--检查登录态--点击设置按钮--上划--点击退出--点击确认退出
            返回值：
                0：当前还在登录态，登出失败
                1：当前不在登录态，登出成功"""
        log_utils.C_INFO('开始登出')

        self.wait_element_by_mode(base_data.wait_time_long,By.ID,self.more_button_id,'更多按钮')
        self.click_more_button()
        self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.setting_container_id,'更多菜单')
        log_utils.C_STEP('检查登录态')
        if self.check_is_login_in_more_page() == 0:
            log_utils.F_ERROR('没有在登陆态，先去退出登录')
            self.reset_app()
            if self.login_test() == 0:
                log_utils.F_ERROR('登录功能已经失效！无法继续测试！')
                self.tear_down()
                sys.exit(-1)
            else:
                log_utils.C_INFO('登录成功，继续测试！')
                self.reset_app()
                log_utils.C_INFO('开始登出')
                self.wait_element_by_mode(base_data.wait_time_long,By.ID,self.more_button_id,'更多按钮')
                self.click_more_button()
                self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.setting_container_id,'更多菜单')

        self.click_setting_container()
        self.my_sleep(3)
        log_utils.C_STEP('上划屏幕')
        self.my_swipe('up')
        self.screenshot('设置页面截图')
        self.click_signout_button_first()
        self.my_sleep()
        self.click_signout_button_second()
        self.my_sleep()
        self.click_yes_button()

        self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.more_button_id,'回到主页')
        log_utils.C_STEP('验证是否登出成功，点击更多按钮')
        self.click_more_button()
        self.screenshot('登录状态截图')
        if self.check_is_login_in_more_page() == 1:
            log_utils.F_FAIL('在登录态，登出失败')
            return 0
        else:
            log_utils.P_PASS('不在登录态，登出成功')
            return 1





    def login_test(self):
        """功能：
                太合登录，正常情况，输入正确的账号密码
            返回值：
                1：登录成功
                0：登录失败"""

        log_utils.C_INFO('开始测试登录功能')
        self.after_login()
        if self.taihe_login(1) == 1:
            log_utils.P_PASS('登录成功！测试通过')
            return 1
        else:
            log_utils.F_FAIL('登录失败！测试失败')
            return 0

