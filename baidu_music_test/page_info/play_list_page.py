# -*- coding:utf-8 -*-
#此页面是歌单页面
from selenium.webdriver.common.by import By
from baidu_music_test.utils import log_utils
from baidu_music_test.utils.base_utils import base_utils


class play_list_page(base_utils):
    play_list_page_play_list_name_id = 'com.ting.mp3.android:id/tv_playlist_name'           #歌单名
    play_list_page_favorite_button_id = 'com.ting.mp3.android:id/favorite_playlist_layout'  #收藏按钮
    play_list_page_play_all_button_id = 'com.ting.mp3.android:id/random_play'               #播放全部按钮
    play_list_page_download_button_id = 'com.ting.mp3.android:id/header_batch_download'     #缓存按钮

    play_list_page_first_song_name_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/view_listview\"]\
            /android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]\
            /android.widget.LinearLayout[1]/android.widget.TextView[1]"                     #第一首歌曲的歌曲名
    play_list_page_third_song_name_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/view_listview\"]\
            /android.widget.RelativeLayout[4]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]\
            /android.widget.LinearLayout[1]/android.widget.TextView[1]"                     #第三首歌曲的歌曲名

    def get_play_list_page_name(self):
        return self.find_element_and_action(By.ID,self.play_list_page_play_list_name_id,self.action.get_text,'当前歌单名')

    def get_play_list_page_first_song_name(self):
        return self.find_element_and_action(By.XPATH,self.play_list_page_first_song_name_xpath,self.action.get_text,'第一首歌曲的歌曲名')

    def get_play_list_page_third_song_name(self):
        return self.find_element_and_action(By.XPATH,self.play_list_page_third_song_name_xpath,self.action.get_text,'第三首歌曲的歌曲名')

    def click_play_list_page_third_song_to_play(self):
        if not self.find_element_and_action(By.XPATH,self.play_list_page_third_song_name_xpath,self.action.click,'第三首歌曲条目') == 0:
            log_utils.F_ERROR('点击失败')
            return 1

    def click_play_list_page_play_all_button(self):
        if not self.find_element_and_action(By.ID,self.play_list_page_play_all_button_id,self.action.click,'播放全部按钮') == 0:
            log_utils.F_ERROR('点击失败')
            return 1
