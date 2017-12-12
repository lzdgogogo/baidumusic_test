# -*- coding:utf-8 -*-
#此页面是评论页面
from selenium.webdriver.common.by import By
from baidu_music_test.utils import log_utils
from baidu_music_test.utils.base_utils import base_utils


class comment_page(base_utils):
    comment_page_title_bar_title_id = 'com.ting.mp3.android:id/title_bar_title'         #标题栏
    comment_page_title_bar_back_button_id = 'com.ting.mp3.android:id/title_bar_back'    #返回按钮

    def click_comment_page_title_bar_back_button(self):
        """点击评论页面的返回按钮"""
        if not self.find_element_and_action(By.ID,self.comment_page_title_bar_back_button_id,self.action.click,'返回按钮') == 0:
            log_utils.F_ERROR('点击失败')
            return 1

    def get_comment_page_title_bar_title_text(self):
        """获取评论页的标题
        返回值：
            1：获取失败
            title：正常结果"""
        title = self.find_element_and_action(By.ID,self.comment_page_title_bar_title_id,self.action.get_text,'评论页的标题')
        if title == 1 or title == 2:
            log_utils.C_INFO('获取文本失败')
            self.screenshot('获取评论页的标题失败')
            return 1
        return title
