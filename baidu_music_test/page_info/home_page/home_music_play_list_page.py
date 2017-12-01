# -*- coding:utf-8 -*-
#主页--音乐分栏--歌单页面
#此页面是歌单页面，主要包括上方的标题栏，下面的歌单部分，布局类似“田”
from selenium.webdriver.common.by import By
from baidu_music_test.page_info.home_page.home_music_page import home_music_page
from baidu_music_test.utils import log_utils


class home_music_play_list_page(home_music_page):
    def __init__(self):
        super().__init__()

    play_list_page_hottest_button_id = 'com.ting.mp3.android:id/playlist_hot'   #歌单上面的最热按钮
    play_list_page_newest_button_id = 'com.ting.mp3.android:id/playlist_new'    #歌单上面的最新按钮

    play_list_page_first_play_list_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/view_listview\"]\
        /android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]"                                 #第一个歌单的布局，点击这里可以进入歌单页面
    play_list_page_first_play_list_play_button_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/view_listview\"]\
        /android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[3]"     #歌单页面上的左上方的歌单的播放按钮
    play_list_page_first_play_list_name_xpath = "//android.support.v4.view.ViewPager[1]/android.widget.RelativeLayout[1]\
        /android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]\
        /android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]\
        /android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]\
        /android.widget.RelativeLayout[1]/android.widget.TextView[2]"                                       #第一个歌单的歌单名称

    def click_play_list_page_first_play_list(self):
        """功能：
                点击第一个歌单的布局来进入歌单页面"""
        if not self.find_element_and_action(By.XPATH,self.play_list_page_first_play_list_xpath,self.action.click,'第一个歌单') == 0:
            log_utils.F_ERROR('点击第一个榜单失败')
            return 1

    def get_play_list_page_first_play_list_name(self):
        """功能：
                获取第一个歌单的歌单名"""
        return self.find_element_and_action(By.XPATH,self.play_list_page_first_play_list_name_xpath,self.action.get_text,'第一个歌单的歌单名')

    def click_play_list_page_first_play_list_play_button(self):
        """功能：
                点击第一个歌单的播放按钮"""
        if not self.find_element_and_action(By.XPATH,self.play_list_page_first_play_list_play_button_xpath,self.action.click,'第一个歌单的播放按钮') == 0:
            log_utils.F_ERROR('点击第一个榜单的播放按钮失败')
            return 1