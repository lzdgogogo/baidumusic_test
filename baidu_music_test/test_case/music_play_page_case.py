# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from baidu_music_test.data import base_data
from baidu_music_test.page_info.home_page.home_music_play_list_page import home_music_play_list_page
from baidu_music_test.page_info.play_page.lyric_page import lyric_page
from baidu_music_test.page_info.play_page.music_play_page import music_play_page
from baidu_music_test.utils import log_utils


class music_play_page_case(home_music_play_list_page,music_play_page,lyric_page):
    def music_play_page_UI_test(self):
        """UI展示：歌曲播放页的各项展示功能，依次是专辑图、返回按钮、播放次数、当前播放时间、总时长、歌曲名、歌手名、歌词按钮、
        缓存按钮、喜欢按钮、分享按钮、更多按钮、播放模式按钮、上一曲按钮、播放暂停按钮、下一曲按钮、播放列表按钮、
        相关明星、相似歌曲、推荐歌单、精彩热评。
        返回值：
            0：测试通过
            1：进入歌单页面失败
            2：进入歌曲播放页失败
            3：某控件显示错误"""
        home_music_play_list_page.click_play_list_button(self)
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.play_list_page_newest_button_id,'进入歌单页面') == 1:
            return 1

        home_music_play_list_page.click_play_list_page_first_play_list_play_button(self)
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,music_play_page.music_play_page_album_pic_id,'进入歌曲播放页') == 1:
            return 2

        log_utils.C_STEP('开始测试歌曲播放页的各项展示功能，依次是专辑图、返回按钮、播放次数、当前播放时间、总时长、歌曲名、歌手名、歌词按钮、\
缓存按钮、喜欢按钮、分享按钮、更多按钮、播放模式按钮、上一曲按钮、播放暂停按钮、下一曲按钮、播放列表按钮、\
相关明星、相似歌曲、推荐歌单、精彩热评。')
        value_list = {0: music_play_page.is_music_play_page_album_pic_displayed(self),
                      1: music_play_page.is_music_play_page_back_button_displayed(self),
                      2: music_play_page.is_music_play_page_play_count_displayed(self),
                      3: music_play_page.is_music_play_page_current_time_text_displayed(self),
                      4: music_play_page.is_music_play_page_total_time_text_displayed(self),
                      5: music_play_page.is_music_play_page_song_name_text_displayed(self),
                      6: music_play_page.is_music_play_page_artist_name_text_displayed(self),
                      7: music_play_page.is_music_play_page_lyric_button_displayed(self),
                      8: music_play_page.is_music_play_page_download_button_displayed(self),
                      9: music_play_page.is_music_play_page_fav_button_displayed(self),
                      10: music_play_page.is_music_play_page_share_button_displayed(self),
                      11: music_play_page.is_music_play_page_more_button_displayed(self),
                      12: music_play_page.is_music_play_page_play_mode_button_displayed(self),
                      13: music_play_page.is_music_play_page_prev_song_button_displayed(self),
                      14: music_play_page.is_music_play_page_music_play_pause_button_displayed(self),
                      15: music_play_page.is_music_play_page_next_song_button_displayed(self),
                      16: music_play_page.is_music_play_page_play_list_button_displayed(self)}
        self.my_sleep(2)

        log_utils.C_STEP('滑动半个屏幕')
        self.my_swipe('up',1000)
        self.my_sleep(5)

        value_list[17] = music_play_page.is_music_play_page_relative_star_title_displayed(self)
        value_list[18] = music_play_page.is_music_play_page_relative_song_title_displayed(self)

        log_utils.C_STEP('滑动半个屏幕')
        self.my_swipe('up',700)
        self.my_sleep(5)

        value_list[19] = music_play_page.is_music_play_page_recommend_play_list_title_displayed(self)
        value_list[20] = music_play_page.is_music_play_page_hot_comment_title_displayed(self)

        i = 0
        while i < 21:
            if not value_list[i] == 0:
                return 3
            i += 1

        return 0

    def music_play_page_album_test(self):
        """测试点击专辑图会不会进入歌词页，点击歌词按钮进入歌词页
        返回值：
            0：正常
            1：进入歌单页面失败
            2：进入歌曲播放页失败
            3：点击专辑图进入了歌词页面（不应该进入）
            4：点击了歌词按钮没有进入歌词页面"""

        home_music_play_list_page.click_play_list_button(self)
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.play_list_page_newest_button_id,'进入歌单页面') == 1:
            return 1

        home_music_play_list_page.click_play_list_page_first_play_list_play_button(self)
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,music_play_page.music_play_page_album_pic_id,'进入歌曲播放页') == 1:
            return 2

        music_play_page.click_music_play_page_album(self)
        self.my_sleep(5)
        if self.find_element_and_action(By.ID,lyric_page.lyric_page_back_button_id,self.action.is_displayed,'歌词页面') == 0:
            return 3

        music_play_page.click_music_play_page_lyric_button(self)
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.lyric_page_back_button_id,'进入歌词页面') == 1:
            return 4

        return 0