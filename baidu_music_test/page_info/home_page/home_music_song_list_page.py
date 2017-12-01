# -*- coding:utf-8 -*-
#首页--音乐分栏--榜单分栏
#此页面的主要部分是一个list，每个部分都是一个相同的布局，包括了榜单图片、榜单歌曲前三名、一个进入榜单按钮
#榜单图片部分包括一个榜单图片和一个播放按钮
#榜单歌曲前三名包括三个text
from selenium.webdriver.common.by import By
from baidu_music_test.page_info.home_page.home_music_page import home_music_page
from baidu_music_test.utils import log_utils


class home_music_song_list_page(home_music_page):
    def __init__(self):
        super().__init__()

    first_song_list_play_all_button_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/swipe_target\"]\
                                /android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]"     #第一个榜单的播放全部按钮
    second_song_list_play_all_button_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/swipe_target\"]\
                                /android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]"     #第二个榜单的播放全部按钮

    first_song_list_top3_title1_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/swipe_target\"]\
                                /android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[@index=\"0\"]"        #第一个榜单的歌曲top3的第一首歌名,不知道为啥，这三个定位不到
    first_song_list_top3_title2_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/swipe_target\"]\
                                /android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[2]"        #第一个榜单的歌曲top3的第二首歌名
    first_song_list_top3_title3_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/swipe_target\"]\
                                /android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[3]"        #第一个榜单的歌曲top3的第三首歌名

    first_song_list_list_enter_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/swipe_target\"]\
                                /android.widget.RelativeLayout[1]/android.widget.ImageView[1]"                                      #第一个榜单的‘>’按钮,点击能进入榜单

    def click_first_song_list_play_all_button(self):
        """功能：
                点击第一个榜单的播放全部按钮"""
        if not self.find_element_and_action(By.XPATH,self.first_song_list_play_all_button_xpath,self.action.click,'第一个榜单的播放全部按钮') == 0:
            log_utils.F_ERROR('点击播放全部按钮失败')
            return 1

    def click_second_song_list_play_all_button(self):
        """功能：
                点击第二个榜单的播放全部按钮"""
        if not self.find_element_and_action(By.XPATH,self.second_song_list_play_all_button_xpath,self.action.click,'第二个榜单的播放全部按钮') == 0:
            log_utils.F_ERROR('点击播放全部按钮失败')
            return 1

    def click_first_song_list_enter_button(self):
        """功能：
                点击第一个榜单的'>'按钮，来进入第一个榜单的榜单页面"""
        if not self.find_element_and_action(By.XPATH,self.first_song_list_list_enter_xpath,self.action.click,'第一个榜单的\'>\'按钮') == 0:
            log_utils.F_ERROR('点击一个榜单的\'>\'按钮失败')
            return 1

    def get_frist_song_list_frist_song_name(self):
        """功能：
                获取第一个榜单的第一首歌曲的歌曲名"""
        return self.find_element_and_action(By.XPATH,self.first_song_list_top3_title1_xpath,self.action.get_text,'第一首歌曲的歌曲名')