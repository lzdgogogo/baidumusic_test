# -*- coding:utf-8 -*-
#今日推荐页
from selenium.webdriver.common.by import By
from baidu_music_test.utils import log_utils
from baidu_music_test.utils.base_utils import base_utils


class today_commend_page(base_utils):
    today_commend_page_play_all_button_id = 'com.ting.mp3.android:id/txt_play'      #播放全部按钮
    today_commend_page_second_song_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/view_listview\"]\
                        /android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]"   #第二首歌曲

    def click_today_commend_page_play_all_button(self):
        if not self.find_element_and_action(By.ID,self.today_commend_page_play_all_button_id,self.action.click,'播放全部按钮') == 0:
            log_utils.F_ERROR('点击播放全部按钮失败')
            return 1

    def click_today_commend_page_second_song(self):
        if not self.find_element_and_action(By.XPATH,self.today_commend_page_second_song_xpath,self.action.click,'第二首歌曲') == 0:
            log_utils.F_ERROR('点击第二首歌曲失败')
            return 1