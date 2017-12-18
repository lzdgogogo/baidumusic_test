from selenium.webdriver.common.by import By
from baidu_music_test.utils import log_utils
from baidu_music_test.utils.base_utils import base_utils
# -*- coding:utf-8 -*-
#6.0.5版本大改后的播放页面

class music_play_page(base_utils):
    music_play_page_album_pic_id = 'com.ting.mp3.android:id/img_head_album'             #上方专辑图
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
    music_play_page_play_mode_button_id = 'com.ting.mp3.android:id/btn_mode'            #播放模式按钮
    music_play_page_play_list_button_id = 'com.ting.mp3.android:id/btn_list'            #播放列表按钮
    music_play_page_play_count_id = 'com.ting.mp3.android:id/tv_play_count'             #播放次数
    music_play_page_relative_star_title_xpath = "//android.widget.FrameLayout[@resource-id=\"com.ting.mp3.android:id/layout_relative_star\"]\
                    /android.widget.RelativeLayout[1]/android.widget.TextView[1]"          #相关明星的标题(相似歌曲，推荐歌单的id跟这个一样)
    music_play_page_relative_song_title_xpath = "//android.widget.FrameLayout[@resource-id=\"com.ting.mp3.android:id/layout_similar_songs\"]\
                    /android.widget.RelativeLayout[1]/android.widget.TextView[1]"           #相似歌曲的标题
    music_play_page_recommend_play_list_title_xpath = "//android.widget.FrameLayout[@resource-id=\"com.ting.mp3.android:id/layout_relative_songlist\"]\
                    /android.widget.RelativeLayout[1]/android.widget.TextView[1]"           #推荐歌单的标题
    music_play_page_hot_comment_title_id = 'com.ting.mp3.android:id/title_hot_comment'  #精彩热评的标题

    def get_music_play_page_playing_song_name(self):
        """功能：
                获取正在播放的歌曲名"""
        return self.find_element_and_action(By.ID,self.music_play_page_song_name_text_id,self.action.get_text,'正在播放的歌曲名')

    def get_current_play_time(self):
        """获取当前播放时长"""
        return self.find_element_and_action(By.ID,self.music_play_page_current_time_text_id,self.action.get_text,'获取已播放时长')

    def is_music_play_page_playing_song(self):
        """功能：
                判断是否正在播放歌曲
            返回值：
                0：正在播放
                1：不在播放"""
        log_utils.C_INFO('验证是否正在播放歌曲')
        first_time = self.find_element_and_action(By.ID,self.music_play_page_current_time_text_id,self.action.get_text,'获取已播放时长')
        log_utils.C_INFO('当前已播放时长为：'+first_time+'   睡眠一段时间')
        self.my_sleep(5)
        second_time = self.find_element_and_action(By.ID,self.music_play_page_current_time_text_id,self.action.get_text,'获取已播放时长')
        log_utils.C_INFO('当前已播放时长为：'+second_time)
        if second_time > first_time:
            log_utils.C_INFO('正在播放！')
            return 0
        else:
            log_utils.C_INFO('没在播放！')
            return 1

    def is_music_play_page_album_pic_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_album_pic_id,self.action.is_displayed,'专辑图') == 0:
            return 1
        return 0

    def is_music_play_page_back_button_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_back_button_id,self.action.is_displayed,'返回按钮') == 0:
            return 1
        return 0

    def is_music_play_page_current_time_text_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_current_time_text_id,self.action.is_displayed,'当前播放时长') == 0:
            return 1
        return 0

    def is_music_play_page_total_time_text_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_total_time_text_id,self.action.is_displayed,'总播放时长') == 0:
            return 1
        return 0

    def is_music_play_page_song_name_text_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_song_name_text_id,self.action.is_displayed,'歌曲名') == 0:
            return 1
        return 0

    def is_music_play_page_artist_name_text_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_artist_name_text_id,self.action.is_displayed,'歌手名') == 0:
            return 1
        return 0

    def is_music_play_page_lyric_button_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_lyric_button_id,self.action.is_displayed,'歌词页面按钮') == 0:
            return 1
        return 0

    def is_music_play_page_download_button_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_download_button_id,self.action.is_displayed,'下载按钮') == 0:
            return 1
        return 0

    def is_music_play_page_fav_button_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_fav_button_id,self.action.is_displayed,'喜欢按钮') == 0:
            return 1
        return 0

    def is_music_play_page_share_button_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_share_button_id,self.action.is_displayed,'分享按钮') == 0:
            return 1
        return 0

    def is_music_play_page_more_button_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_more_button_id,self.action.is_displayed,'更多按钮') == 0:
            return 1
        return 0

    def is_music_play_page_music_play_pause_button_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_music_play_pause_button_id,self.action.is_displayed,'播放暂停按钮') == 0:
            return 1
        return 0

    def is_music_play_page_next_song_button_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_next_song_button_id,self.action.is_displayed,'下一首按钮') == 0:
            return 1
        return 0

    def is_music_play_page_prev_song_button_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_prev_song_button_id,self.action.is_displayed,'上一曲按钮') == 0:
            return 1
        return 0

    def is_music_play_page_play_mode_button_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_play_mode_button_id,self.action.is_displayed,'播放模式按钮') == 0:
            return 1
        return 0

    def is_music_play_page_play_list_button_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_play_list_button_id,self.action.is_displayed,'播放列表按钮') == 0:
            return 1
        return 0

    def is_music_play_page_play_count_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_play_count_id,self.action.is_displayed,'播放次数') == 0:
            return 1
        return 0

    def is_music_play_page_relative_star_title_displayed(self):
        if not self.find_element_and_action(By.XPATH,self.music_play_page_relative_star_title_xpath,self.action.is_displayed,'相关明星') == 0:
            return 1
        return 0

    def is_music_play_page_relative_song_title_displayed(self):
        if not self.find_element_and_action(By.XPATH,self.music_play_page_relative_song_title_xpath,self.action.is_displayed,'相似歌曲') == 0:
            return 1
        return 0

    def is_music_play_page_recommend_play_list_title_displayed(self):
        if not self.find_element_and_action(By.XPATH,self.music_play_page_recommend_play_list_title_xpath,self.action.is_displayed,'推荐歌单') == 0:
            return 1
        return 0

    def is_music_play_page_hot_comment_title_displayed(self):
        if not self.find_element_and_action(By.ID,self.music_play_page_hot_comment_title_id,self.action.is_displayed,'精彩热评') == 0:
            return 1
        return 0

    def click_music_play_page_album(self):
        self.find_element_and_action(By.ID,self.music_play_page_album_pic_id,self.action.click,'专辑图')

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

    def click_music_play_page_play_pause_button(self,str):
        self.find_element_and_action(By.ID,self.music_play_page_music_play_pause_button_id,self.action.click,str)

    def click_music_play_page_next_song_button(self):
        self.find_element_and_action(By.ID,self.music_play_page_next_song_button_id,self.action.click,'下一曲按钮')

    def click_music_play_page_prev_song_button(self):
        self.find_element_and_action(By.ID,self.music_play_page_prev_song_button_id,self.action.click,'上一曲按钮')