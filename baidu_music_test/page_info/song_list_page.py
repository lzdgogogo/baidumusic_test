# -*- coding:utf-8 -*-
#大部分的榜单页面元素，例如：新歌榜
#此页面是一个大list，第一栏是榜单图片为背景，包括一个返回按钮，一个分享按钮，一个更新日期text
#第二栏是一个播放全部按钮，一个批量缓存按钮
#从第三栏开始往下就都是歌曲信息
#注意在此页面的元素信息都是初始状态，当页面进行滑动之后，歌曲的信息会发生变化，xpath的序号会发生变化，因此在此页面不要进行滑动的动作
from selenium.webdriver.common.by import By
from baidu_music_test.utils import log_utils
from baidu_music_test.utils.base_utils import base_utils


class song_list_page(base_utils):
    def __init__(self):
            super().__init__()

    song_list_page_return_button_id = 'com.ting.mp3.android:id/head_return'                     #返回按钮
    song_list_page_share_button_id = 'com.ting.mp3.android:id/share_btn'                        #分享按钮
    song_list_page_play_all_button_id = 'com.ting.mp3.android:id/txt_play'                      #播放全部按钮
    song_list_page_download_list_button_id = 'com.ting.mp3.android:id/img_download_list'        #缓存按钮，点击后会进入批量缓存页

    song_list_page_first_song_artist_name_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/view_listview\"]\
                                                    /android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]\
                                                    /android.widget.LinearLayout[1]/android.widget.LinearLayout[1]\
                                                    /android.widget.LinearLayout[2]/android.widget.TextView[1]"         #第一个首歌的歌手名

    song_list_page_first_song_name_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/view_listview\"]\
                                                     /android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]\
                                                     /android.widget.LinearLayout[1]/android.widget.LinearLayout[1]\
                                                     /android.widget.LinearLayout[1]/android.widget.TextView[1]"        #第一首歌的歌名

    song_list_page_first_song_more_button_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/view_listview\"]\
                                                    /android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]\
                                                    /android.widget.RelativeLayout[1]"                                  #第一首歌的更多按钮

    song_list_page_third_song_name_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/view_listview\"]\
                                                    /android.widget.RelativeLayout[4]/android.widget.LinearLayout[1]\
                                                    /android.widget.LinearLayout[1]/android.widget.LinearLayout[1]\
                                                    /android.widget.LinearLayout[1]/android.widget.TextView[1]"         #第三首歌的歌名
    song_list_page_third_song_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/view_listview\"]\
                                                    /android.widget.RelativeLayout[4]"                                  #第三首歌的整体布局，点击这个可以播放第三首歌

    def get_first_song_list_third_song_name(self):
        """功能：
                返回第三首歌的歌曲名"""
        return self.find_element_and_action(By.XPATH,self.song_list_page_third_song_name_xpath,self.action.get_text,'获取第三首歌的歌曲名')

    def click_third_song_to_play_third_song(self):
        """功能：
                通过点击第三首歌的布局来开始播放第三首歌"""
        if not self.find_element_and_action(By.XPATH,self.song_list_page_third_song_xpath,self.action.click,'第三首歌的布局') == 0:
            log_utils.F_ERROR('点击第三首歌的布局失败')
            return 1

    def get_first_song_list_first_song_name(self):
        """功能：
                返回第一首歌的歌曲名"""
        return self.find_element_and_action(By.XPATH,self.song_list_page_first_song_name_xpath,self.action.get_text,'获取第一首歌的歌曲名')

    def click_song_list_play_all_button(self):
        """功能：
                点击榜单页面的播放全部按钮"""
        if not self.find_element_and_action(By.ID,self.song_list_page_play_all_button_id,self.action.click,'点击榜单页面的播放全部按钮') == 0:
            log_utils.F_ERROR('点击榜单页面的播放全部按钮失败')
            return 1

