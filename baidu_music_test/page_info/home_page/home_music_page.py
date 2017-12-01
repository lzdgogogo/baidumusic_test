from selenium.webdriver.common.by import By
from baidu_music_test.page_info.home_page.home_page import home_page
# -*- coding:utf-8 -*-

#百度音乐app的首页，首页的音乐分栏
from baidu_music_test.utils import log_utils


class home_music_page(home_page):
        def __init__(self):
            super().__init__()

        #上边栏
        search_layout_id = 'com.ting.mp3.android:id/search_layout'                                                        #搜索栏
        #搜索栏下方边栏
        recommend_xpath = "//android.widget.HorizontalScrollView[@resource-id=\"com.ting.mp3.android:id/tabsLayout\"]\
                            /android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]"      #搜索栏下方推荐按钮
        song_sheet_xpath = "//android.widget.LinearLayout/android.widget.TextView[2]"       #歌单按钮
        song_list_xpath = "//android.widget.LinearLayout/android.widget.TextView[3]"        #榜单按钮
        video_xpath = "//android.widget.LinearLayout/android.widget.TextView[4]"            #视频按钮
        brand_xpath = "//android.widget.LinearLayout/android.widget.TextView[5]"            #厂牌专区按钮

        def click_song_list_button(self):
            if not self.find_element_and_action(By.XPATH,self.song_list_xpath,self.action.click,'榜单按钮') == 0:
                log_utils.F_ERROR('点击榜单按钮失败')
                return 1

        def click_play_list_button(self):
            if not self.find_element_and_action(By.XPATH,self.song_sheet_xpath,self.action.click,'歌单按钮') == 0:
                log_utils.F_ERROR('点击歌单按钮失败')
                return 1

