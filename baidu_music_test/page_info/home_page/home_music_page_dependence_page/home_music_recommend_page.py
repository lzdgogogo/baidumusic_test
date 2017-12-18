# -*- coding:utf-8 -*-

#音乐--推荐页
from selenium.webdriver.common.by import By
from baidu_music_test.page_info.home_page.home_music_page import home_music_page
from baidu_music_test.utils import log_utils


class home_music_recommend_page(home_music_page):
    home_music_recommend_page_today_recommend_id = 'com.ting.mp3.android:id/day_tv'     #今日推荐图片

    def click_today_recommend_button(self):
        if not self.find_element_and_action(By.ID,self.home_music_recommend_page_today_recommend_id,self.action.click,'今日推荐') == 0:
            log_utils.F_ERROR('点击今日推荐失败')
            return 1
