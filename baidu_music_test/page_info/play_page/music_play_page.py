from selenium.webdriver.common.by import By
from baidu_music_test.utils import log_utils
from baidu_music_test.utils.base_utils import base_utils
# -*- coding:utf-8 -*-
#6.0.5版本大改后的播放页面

class music_play_page(base_utils):
    music_play_page_back_button_id = 'com.ting.mp3.android:id/img_back'                 #返回按钮
    music_play_page_current_time_text_id = 'com.ting.mp3.android:id/tv_current_time'    #当前播放时间
    music_play_page_total_time_text_id = 'com.ting.mp3.android:id/tv_total_time'        #总播放时间
    music_play_page_song_name_text_id = 'com.ting.mp3.android:id/tv_song_name'          #歌曲名
    music_play_page_artist_name_text_id = 'com.ting.mp3.android:id/tv_artist_name'      #歌手名
    music_play_page_lyric_button_id = 'com.ting.mp3.android:id/btn_lyric'               #歌词页面按钮
    music_play_page_download_button_id = 'com.ting.mp3.android:id/btn_download'         #下载按钮
    music_play_page_fav_button_id = 'com.ting.mp3.android:id/btn_fav'                   #喜欢按钮
    music_play_page_share_button_id = 'com.ting.mp3.android:id/btn_share'               #分享按钮
    music_play_page_more_button_id = 'com.ting.mp3.android:id/btn_more'                 #更多按钮
    music_play_page_music_play_pause_button_id = 'com.ting.mp3.android:id/btn_play'     #播放暂停按钮
    music_play_page_next_song_button_id = 'com.ting.mp3.android:id/btn_next'            #下一曲按钮
    music_play_page_prev_song_button_id = 'com.ting.mp3.android:id/btn_prev'            #上一曲按钮

    def get_music_play_page_playing_song_name(self):
        """功能：
                获取正在播放的歌曲名"""
        return self.find_element_and_action(By.ID,self.music_play_page_song_name_text_id,self.action.get_text,'正在播放的歌曲名')

    def is_music_play_page_playing_song(self):
        """功能：
                判断是否正在播放歌曲
            返回值：
                0：正在播放
                1：不在播放"""
        log_utils.C_INFO('验证是否正在播放歌曲')
        first_time = self.find_element_and_action(By.ID,self.music_play_page_current_time_text_id,self.action.get_text,'获取已播放时长')
        log_utils.C_INFO('当前已播放时长为：'+first_time+'   接下来睡眠10秒')
        self.my_sleep(10)
        second_time = self.find_element_and_action(By.ID,self.music_play_page_current_time_text_id,self.action.get_text,'获取已播放时长')
        log_utils.C_INFO('当前已播放时长为：'+second_time)
        if second_time > first_time:
            log_utils.C_INFO('正在播放！')
            return 0
        else:
            log_utils.C_INFO('没在播放！')
            return 1


    def click_music_play_page_back_button(self):
        self.find_element_and_action(By.ID,self.music_play_page_back_button_id,self.action.click,'返回按钮')

    def click_music_play_page_lyric_button(self):
        self.find_element_and_action(By.ID,self.music_play_page_lyric_button_id,self.action.click,'歌词按钮')

    def click_music_play_page_download_button(self):
        self.find_element_and_action(By.ID,self.music_play_page_download_button_id,self.action.click,'下载按钮')

    def click_music_play_page_fav_button(self):
        self.find_element_and_action(By.ID,self.music_play_page_fav_button_id,self.action.click,'喜欢按钮')

    def click_music_play_page_share_button(self):
        self.find_element_and_action(By.ID,self.music_play_page_share_button_id,self.action.click,'分享按钮')

    def click_music_play_page_more_button(self):
        self.find_element_and_action(By.ID,self.music_play_page_more_button_id,self.action.click,'更多按钮')

    def click_music_play_page_pley_pause_button(self):
        self.find_element_and_action(By.ID,self.music_play_page_music_play_pause_button_id,self.action.click,'播放按钮')

    def click_music_play_page_next_song_button(self):
        self.find_element_and_action(By.ID,self.music_play_page_next_song_button_id,self.action.click,'下一曲按钮')

    def click_music_play_page_prev_song_button(self):
        self.find_element_and_action(By.ID,self.music_play_page_prev_song_button_id,self.action.click,'上一曲按钮')