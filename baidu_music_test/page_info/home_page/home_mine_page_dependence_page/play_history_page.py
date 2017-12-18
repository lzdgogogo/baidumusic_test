# -*- coding:utf-8 -*-
#点击最近播放后进入的最近播放页
from selenium.webdriver.common.by import By
from baidu_music_test.utils import log_utils
from baidu_music_test.utils.base_utils import base_utils


class play_history_page(base_utils):
    play_history_page_song_text_id = 'com.ting.mp3.android:id/local_song_text'      #上方歌曲

    play_history_page_third_song_layout_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/playlist_list_songs\"]\
        /android.widget.RelativeLayout[4]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]"    #列表中第三首歌曲

    def click_play_history_page_third_song_layout_to_play(self):
        if not self.find_element_and_action(By.XPATH,self.play_history_page_third_song_layout_xpath,self.action.click,'第三首歌曲') == 0:
            log_utils.F_ERROR('点击第三首歌曲失败')
            return 1
