# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from baidu_music_test.data import base_data
from baidu_music_test.page_info.home_page.home_music_song_list_page import home_music_song_list_page
from baidu_music_test.page_info.play_page.music_play_page import music_play_page
from baidu_music_test.page_info.song_list_page import song_list_page
from baidu_music_test.utils import log_utils


class song_list_case(home_music_song_list_page,song_list_page,music_play_page):

    def song_list_play_test(self):
        """功能：
                测试音乐-榜单页面的播放歌曲的功能，榜单页面的播放歌曲功能（有两个播放全部按钮和点击歌曲条目播放的功能）
            步骤：
                1.进入音乐--榜单页面
                2.获取第一个榜单的第一首歌曲的歌曲名
                3.点击第一个榜单的播放全部按钮
                4.在跳转到的歌曲播放页中验证正在播放的歌曲是否与第一首歌曲歌名一致
                5.点击第一个榜单的‘>’按钮进入第一个榜单页面
                6.获取第三首歌的歌名，并且点击第三首歌条目
                7.在跳转到的歌曲播放页中验证正在播放的歌曲是否与第三首歌曲歌名一致
                8.点击返回按钮返回榜单页面
                9.获取第一首歌名，并且名点击全部播放按钮
                10.在跳转到的歌曲播放页中验证正在播放的歌曲是否与第一首歌曲歌名一致
            返回值：
                3：获取某歌曲名失败，测试失败
                2：等待某控件超时，测试失败
                1：测试失败
                0：测试成功"""
        flag = 0
        log_utils.C_INFO('开始测试音乐--榜单和榜单页面的播放功能')
        self.click_song_list_button()
        if self.wait_element_by_mode(base_data.wait_time_mid,By.XPATH,self.first_song_list_play_all_button_xpath,'进入榜单页面') == 1:
            return 2
        tmp = self.get_frist_song_list_frist_song_name()        #将获取到的整串信息分割开，提取到歌曲名
        tmp_list = tmp.split(' ')
        first_song_name = tmp_list[1]
        if first_song_name == 1 or first_song_name == 2:
            log_utils.F_ERROR('获取歌曲名失败，无法继续测试')
            return 3
        log_utils.C_STEP('第一个榜单的第一首歌曲名为：'+first_song_name)

        self.click_first_song_list_play_all_button()
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.music_play_page_artist_name_text_id,'进入歌曲播放页') == 1:
            return 2
        self.my_sleep(2)
        playing_song_name = self.get_music_play_page_playing_song_name()
        if playing_song_name == 1 or playing_song_name == 2:
            log_utils.F_ERROR('获取歌曲名失败，无法继续测试')
            return 3
        log_utils.C_STEP('正在播放的歌曲名是：'+playing_song_name)
        self.is_music_play_page_playing_song()
        if first_song_name == playing_song_name:
            log_utils.P_PASS('两个歌曲名一致，播放第一首歌曲成功，音乐--榜单页面的全部播放按钮功能完好')
        else:
            log_utils.F_FAIL('两个歌曲名不一致，播放第一首歌曲失败，音乐--榜单页面的全部播放按钮功能损坏')
            flag = 1

        self.click_music_play_page_back_button()
        self.my_sleep(3)
        self.click_first_song_list_enter_button()
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.song_list_page_play_all_button_id,'进入第一个榜单的榜单页面') == 1:
            return 2
        third_song_name = self.get_first_song_list_third_song_name()
        if third_song_name == 1 or third_song_name == 2:
            log_utils.F_ERROR('获取歌曲名失败，无法继续测试')
            return 3
        log_utils.C_STEP('第一个榜单的第三首歌曲名为：'+third_song_name)

        self.click_third_song_to_play_third_song()
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.music_play_page_artist_name_text_id,'进入歌曲播放页') == 1:
            return 2
        self.my_sleep(2)
        playing_song_name = self.get_music_play_page_playing_song_name()
        if playing_song_name == 1 or playing_song_name == 2:
            log_utils.F_ERROR('获取歌曲名失败，无法继续测试')
            return 3
        log_utils.C_STEP('正在播放的歌曲名是： '+playing_song_name)
        self.is_music_play_page_playing_song()
        if third_song_name == playing_song_name:
            log_utils.P_PASS('两个歌曲名一致，播放第三首歌曲成功，点击榜单页面的歌曲来播放功能完好')
        else:
            log_utils.F_FAIL('两个歌曲名不一致，播放第三首歌曲失败，点击榜单页面的歌曲来播放功能损坏')
            flag = 1

        self.click_music_play_page_back_button()
        self.my_sleep(3)
        first_song_name = self.get_first_song_list_first_song_name()
        if first_song_name == 1 or first_song_name == 2:
            log_utils.F_ERROR('获取歌曲名失败，无法继续测试')
            return 3
        log_utils.C_STEP('第一首歌曲的歌曲名为：'+first_song_name)
        self.click_song_list_play_all_button()
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.music_play_page_artist_name_text_id,'进入歌曲播放页') == 1:
            return 2
        self.my_sleep(2)
        playing_song_name = self.get_music_play_page_playing_song_name()
        if playing_song_name == 1 or playing_song_name == 2:
            log_utils.F_ERROR('获取歌曲名失败，无法继续测试')
            return 3
        log_utils.C_STEP('正在播放的歌曲名是： '+playing_song_name)
        self.is_music_play_page_playing_song()
        if first_song_name == playing_song_name:
            log_utils.P_PASS('两个歌曲名一致，播放第一首歌曲成功，点击榜单页面的播放全部按钮来播放功能完好')
        else:
            log_utils.F_FAIL('两个歌曲名不一致，播放第一首歌曲失败，点击榜单页面的播放全部按钮来播放功能损坏')
            flag = 1


        if flag == 1:
            return 1

        return 0








