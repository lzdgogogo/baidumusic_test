# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from baidu_music_test.data import base_data
from baidu_music_test.page_info.home_page.home_mine_page import home_mine_page
from baidu_music_test.page_info.home_page.home_mine_page_dependence_page.play_history_page import play_history_page
from baidu_music_test.page_info.home_page.home_music_page_dependence_page.home_music_play_list_page import home_music_play_list_page
from baidu_music_test.page_info.home_page.home_music_page_dependence_page.home_music_recommend_page import home_music_recommend_page
from baidu_music_test.page_info.home_page.home_music_page_dependence_page.home_music_song_list_page import home_music_song_list_page
from baidu_music_test.page_info.home_page.home_music_page_dependence_page.play_list_page import play_list_page
from baidu_music_test.page_info.play_page.lyric_page import lyric_page
from baidu_music_test.page_info.play_page.music_play_page import music_play_page
from baidu_music_test.page_info.home_page.home_music_page_dependence_page.song_list_page import song_list_page
from baidu_music_test.page_info.home_page.home_music_page_dependence_page.today_commend_page import today_commend_page
from baidu_music_test.utils import log_utils
import threading


class music_play_page_case(home_mine_page,home_music_song_list_page,home_music_play_list_page,home_music_recommend_page,music_play_page,lyric_page,today_commend_page,play_list_page,song_list_page,play_history_page):
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
        self.screenshot('歌曲播放页UI显示截图')

        log_utils.C_STEP('滑动半个屏幕')
        self.my_swipe('up',1000)
        self.my_sleep(5)
        self.screenshot('歌曲播放页滑动半屏之后UI显示')
        value_list[17] = music_play_page.is_music_play_page_relative_star_title_displayed(self)
        value_list[18] = music_play_page.is_music_play_page_relative_song_title_displayed(self)

        log_utils.C_STEP('滑动半个屏幕')
        self.my_swipe('up',700)
        self.my_sleep(5)
        self.screenshot('歌曲播放页再次滑动半屏后UI显示')
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

    def click_entrance_can_go_to_music_play_page_test(self):
        """测试点击各个入口（今日推荐、歌单、榜单、最近播放）能否正常进入歌曲播放页
        返回值：
            0：测试通过
            1：进入今日推荐页超时
            2：进入歌曲播放页失败
            3：进入歌单页超时
            4：进入第一个歌单页面超时
            5：进入榜单页面超时
            6：进入第一个榜单页面超时
            7：进入我的页面超时
            8：进入最近播放页"""
        flag = 0
        log_utils.C_STEP('开始测试今日推荐页中的播放全部按钮和点击歌曲能否跳转到歌曲播放页')
        home_music_recommend_page.click_today_recommend_button(self)

        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,today_commend_page.today_commend_page_play_all_button_id,'进入今日推荐页')== 1:
            flag = 1
        if not flag == 1:
            today_commend_page.click_today_commend_page_play_all_button(self)
            if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,music_play_page.music_play_page_album_pic_id,'进入歌曲播放页') == 1:
                flag = 2

            music_play_page.click_music_play_page_back_button(self)
            if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,today_commend_page.today_commend_page_play_all_button_id,'回到今日推荐页')== 1:
                flag = 1

            self.my_sleep(3)
            today_commend_page.click_today_commend_page_second_song(self)
            if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,music_play_page.music_play_page_album_pic_id,'进入歌曲播放页') == 1:
                flag = 2

            music_play_page.click_music_play_page_back_button(self)
            if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,today_commend_page.today_commend_page_play_all_button_id,'回到今日推荐页')== 1:
                flag = 1

            self.driver.press_keycode(4)        #回到首页
            self.my_sleep(3)

        log_utils.C_STEP('开始测试点击歌单中歌曲能否播放歌曲')
        home_music_recommend_page.click_play_list_button(self)
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,home_music_play_list_page.play_list_page_hottest_button_id,'进入歌单页') == 1:
            flag = 3
        if not flag == 3:
            home_music_play_list_page.click_play_list_page_first_play_list(self)    #进入第一个歌单
            if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,play_list_page.play_list_page_play_list_name_id,'进入第一个歌单页') == 1:
                flag = 4
            if not flag == 4:
                play_list_page.click_play_list_page_third_song_to_play(self)
                if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,music_play_page.music_play_page_album_pic_id,'进入歌曲播放页') == 1:
                    flag = 2

                music_play_page.click_music_play_page_back_button(self)
                if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,play_list_page.play_list_page_play_list_name_id,'回到第一个歌单页') == 1:
                    flag = 4

            self.driver.press_keycode(4)    #回到歌单页
            self.my_sleep(3)

        log_utils.C_STEP('开始测试点击榜单中歌曲能否播放歌曲')
        home_music_play_list_page.click_song_list_button(self)
        if self.wait_element_by_mode(base_data.wait_time_mid,By.XPATH,home_music_song_list_page.first_song_list_play_all_button_xpath,'进入榜单页面') == 1:
            flag = 5
        if not flag == 5:
            home_music_song_list_page.click_first_song_list_enter_button(self)
            if self.wait_element_by_mode(base_data.wait_time_mid,By.XPATH,song_list_page.song_list_page_first_song_more_button_xpath,'进入第一个榜单页面') == 1:
                flag = 6
            if not flag == 6:
                song_list_page.click_third_song_to_play_third_song(self)
                if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,music_play_page.music_play_page_album_pic_id,'进入歌曲播放页') == 1:
                    flag = 2

                music_play_page.click_music_play_page_back_button(self)
                if self.wait_element_by_mode(base_data.wait_time_mid,By.XPATH,song_list_page.song_list_page_first_song_more_button_xpath,'回到第一个榜单页') == 1:
                    flag = 6
            self.driver.press_keycode(4)    #回到榜单页
            self.my_sleep(3)

        log_utils.C_STEP('开始测试点击最近播放的歌曲能否播放歌曲')
        home_music_song_list_page.click_mine_button(self)
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,home_mine_page.download_music_id,'进入我的页面') == 1:
            flag = 7
        if not flag == 7:
            self.my_sleep(3)
            home_mine_page.click_play_history_button(self)
            if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,play_history_page.play_history_page_song_text_id,'进入最近播放页') == 1:
                flag = 8
            if not flag == 8:
                play_history_page.click_play_history_page_third_song_layout_to_play(self)
                if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,music_play_page.music_play_page_album_pic_id,'进入歌曲播放页') == 1:
                    flag = 2

                music_play_page.click_music_play_page_back_button(self)
                if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,play_history_page.play_history_page_song_text_id,'回到最近播放页') == 1:
                    flag = 8

            self.driver.press_keycode(4)    #回到我的页
            self.my_sleep(3)
            return flag

    def music_play_page_progress_bar_display(self):
        """播放进度条显示，
            在歌曲名上方，贴在专辑图底边，显示播放时间和总播放时长，播放歌曲时进度条随着播放时间变化，左右拖动显示拖动的时间和总时间点"""
        flag = 0
        log_utils.C_STEP('开始测试播放进度条拖动及显示')
        home_music_recommend_page.click_today_recommend_button(self)

        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,today_commend_page.today_commend_page_play_all_button_id,'进入今日推荐页')== 1:
            flag = 1
        if not flag == 1:
            today_commend_page.click_today_commend_page_play_all_button(self)
            if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,music_play_page.music_play_page_album_pic_id,'进入歌曲播放页') == 1:
                flag = 2

            if not flag == 2:
                first_time = music_play_page.get_current_play_time(self)
                log_utils.C_INFO('当前播放时长为：'+first_time)
                log_utils.C_STEP('开始向右拖动进度条')
                size = self.get_size()
                x_coefficient = 800/size[0]
                y_coefficient = 1280/size[1]
                x1 = 100 * x_coefficient
                x2 = 500 * x_coefficient
                y = 800 * y_coefficient
                self.driver.swipe(x1,y,x2,y,3000)
                self.my_sleep()
                second_time = music_play_page.get_current_play_time(self)
                log_utils.C_INFO('当前播放时长为：'+second_time)
                if second_time > first_time:
                    log_utils.C_INFO('进度条拖动成功')

    def music_play_page_progress_bar_pause_displayed(self):
        """暂停时进度条的拖动显示"""
        flag = 0
        log_utils.C_STEP('开始测试暂停进度条拖动及显示')
        home_music_recommend_page.click_today_recommend_button(self)

        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,today_commend_page.today_commend_page_play_all_button_id,'进入今日推荐页')== 1:
            flag = 1
        if not flag == 1:
            today_commend_page.click_today_commend_page_play_all_button(self)
            if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,music_play_page.music_play_page_album_pic_id,'进入歌曲播放页') == 1:
                flag = 2

            if not flag == 2:
                first_time = music_play_page.get_current_play_time(self)
                log_utils.C_INFO('当前播放时长为：'+first_time)
                self.my_sleep(3)
                music_play_page.click_music_play_page_play_pause_button(self,'暂停按钮')
                self.my_sleep(2)
                log_utils.C_STEP('开始向右拖动进度条')
                size = self.get_size()
                x_coefficient = 800/size[0]
                y_coefficient = 1280/size[1]
                x1 = 100 * x_coefficient
                x2 = 500 * x_coefficient
                y = 800 * y_coefficient
                self.driver.swipe(x1,y,x2,y,3000)
                self.my_sleep()
                second_time = music_play_page.get_current_play_time(self)
                log_utils.C_INFO('当前播放时长为：'+second_time)
                if second_time > first_time:
                    log_utils.C_INFO('进度条拖动成功')
                music_play_page.is_music_play_page_playing_song(self)
        return flag






