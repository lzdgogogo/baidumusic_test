from selenium.webdriver.common.by import By
from baidu_music_test.page_info.page_base import page_base
from baidu_music_test.utils import log_utils

__author__ = '刘子恒'
#百度音乐APP首页，在这个页面中，左上角更多按钮、minibar、下边栏是一直显示的。

class home_page(page_base):
        #上边栏
        more_button_id='com.ting.mp3.android:id/more_layout'                        #左上角更多按钮

        #minibar
        minibar_song_name_id='com.ting.mp3.android:id/mb_text_trackname'            #minibar中歌名
        minibar_singer_name_id='com.ting.mp3.android:id/mb_text_artist'             #歌手名
        minibar_control_button_id='com.ting.mp3.android:id/mb_control'              #播放按钮
        minibar_next_button_id='com.ting.mp3.android:id/mb_next'                    #下一首按钮
        minibar_playlist_button_id='com.ting.mp3.android:id/mb_list'                #列表按钮
        #下边栏
        i_music_id='com.ting.mp3.android:id/i_music'                                 #音乐
        i_anylisten_id='com.ting.mp3.android:id/i_anylisten'                         #随心听
        i_trends_id='com.ting.mp3.android:id/i_trends'                               #动态
        i_mine_id='com.ting.mp3.android:id/i_mine'                                    #我的

        def click_more_button(self):
            """功能：
                    点击更多按钮
                返回值：
                    0：点击失败"""

            if self.find_element_by_mode_click(By.ID,self.more_button_id) == 0:
                log_utils.F_ERROR('点击失败')
                return 0

        def click_music_button(self):
            """功能：
                    点击音乐按钮
                返回值：
                    0：点击失败"""

            if self.find_element_by_mode_click(By.ID,self.i_music_id) == 0:
                log_utils.F_ERROR('点击失败')
                return 0

        def click_anylisten_button(self):
            """功能：
                    点击随身听按钮
                返回值：
                    0：点击失败"""

            if self.find_element_by_mode_click(By.ID,self.i_anylisten_id) == 0:
                log_utils.F_ERROR('点击失败')
                return 0

        def click_trends_button(self):
            """功能：
                    点击动态按钮
                返回值：
                    0：点击失败"""

            if self.find_element_by_mode_click(By.ID,self.i_trends_id) == 0:
                log_utils.F_ERROR('点击失败')
                return 0

        def click_mine_button(self):
            """功能：
                    点击我的按钮
                返回值：
                    0：点击失败"""

            if self.find_element_by_mode_click(By.ID,self.i_mine_id) == 0:
                log_utils.F_ERROR('点击失败')
                return 0