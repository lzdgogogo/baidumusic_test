# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from baidu_music_test.data import base_data
from baidu_music_test.page_info.home_page.home_music_play_list_page import home_music_play_list_page
from baidu_music_test.page_info.play_list_page import play_list_page
from baidu_music_test.page_info.play_page.music_play_page import music_play_page
from baidu_music_test.utils import log_utils


class play_list_case(home_music_play_list_page,music_play_page,play_list_page):


    def play_list_play_test(self):
        """功能：
                验证歌单页面相关的播放功能，歌单封面的播放按钮、歌单内部的播放全部按钮，点击歌曲进行播放
            步骤：
                1.进入APP，点击歌单按钮，进入歌单页面,获取第一个歌单的名称
                2.点击第一个歌单页面封面的播放按钮
                3.进入了歌曲播放页，验证是否正在播放，记录下正在播放的歌曲名称
                4.点击歌曲播放页的返回按钮，返回歌单页面，点击第一个歌单的封面进入第一个歌单页面
                5.获取第一首歌曲的歌曲名，跟之前的歌曲名比较
                6.获取第三首歌曲的歌曲名，点击第三首歌曲条目，比较歌曲名，查看是否在播放，点击返回
                7.回到歌单页，点击播放全部按钮，比较第一首歌曲的歌曲名，查看是否在播放，点击返回
            返回值：
                0：测试通过
                1：等待某控件超时
                2：测试失败不通过
                3：获取某文本失败"""
        flag = 0
        log_utils.C_INFO('开始测试歌单页面相关的播放功能')

        #self.home_music_play_list_page = home_music_play_list_page()
        #home_music_play_list_page.click_play_list_button()
        self.click_play_list_button()
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.play_list_page_newest_button_id,'进入歌单页面') == 1:
            return 1

        first_play_list_name = self.get_play_list_page_first_play_list_name()
        if first_play_list_name == 1 or first_play_list_name == 2:
            log_utils.F_ERROR('获取歌单名失败，无法继续测试')
            return 3
        log_utils.C_STEP('第一个歌单名为：'+first_play_list_name)

        self.click_play_list_page_first_play_list_play_button()
        self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.music_play_page_song_name_text_id,'进入歌曲播放页')
        if self.is_music_play_page_playing_song() == 1:
            log_utils.F_ERROR('歌单封面的播放按钮损坏！')
            flag = 1

        playing_song_name = self.get_music_play_page_playing_song_name()
        if playing_song_name == 1 or playing_song_name == 2:
            log_utils.F_ERROR('获取歌曲名失败，无法继续测试')
            return 3

        self.click_music_play_page_back_button()
        self.my_sleep(2)
        self.click_play_list_page_first_play_list()
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.play_list_page_play_all_button_id,'进入第一个歌单页') == 1:
            return 1

        tmp = self.get_play_list_page_first_play_list_name()
        log_utils.C_STEP('当前页面的歌单名为：'+tmp)
        if tmp == first_play_list_name:
            log_utils.C_INFO('两歌单名相同，进入对应的歌单页面成功')
        else:
            log_utils.F_ERROR('两歌单名不相同，页面不对应')
            return 1

        first_song_name = self.get_play_list_page_first_song_name()
        third_song_name = self.get_play_list_page_third_song_name()
        if first_song_name == 1 or first_song_name == 2 or third_song_name == 1 or third_song_name == 2:
            log_utils.F_ERROR('获取歌曲名失败，无法继续测试')
            return 3
        log_utils.C_INFO('第一首歌曲名为：'+first_song_name)
        log_utils.C_INFO('第三首歌曲名为：'+third_song_name)
        if playing_song_name == first_song_name:
            log_utils.P_PASS('播放歌曲名与第一首歌曲名相同，歌单封面上的播放按钮功能完好')

        self.click_play_list_page_third_song_to_play()
        self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.music_play_page_song_name_text_id,'进入歌曲播放页')
        self.is_music_play_page_playing_song()
        tmp = self.get_music_play_page_playing_song_name()
        log_utils.C_INFO('正在播放的歌曲名为：'+tmp)
        if tmp == third_song_name:
            log_utils.P_PASS('正在播放歌曲与第三首歌曲的歌曲名相同，点击歌曲条目来播放歌曲的功能完好')
        else:
            log_utils.F_FAIL('正在播放歌曲与第三首歌曲的歌曲名不相同，点击歌曲条目来播放歌曲的功能损坏')
            flag = 1

        self.click_music_play_page_back_button()
        self.my_sleep(2)
        self.click_play_list_page_play_all_button()
        self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.music_play_page_song_name_text_id,'进入歌曲播放页')
        self.is_music_play_page_playing_song()
        tmp = self.get_music_play_page_playing_song_name()
        log_utils.C_INFO('正在播放的歌曲名为：'+tmp)
        if tmp == first_song_name:
            log_utils.P_PASS('正在播放歌曲与第一首歌曲的歌曲名相同，点击播放全部按钮来播放歌曲的功能完好')
        else:
            log_utils.F_FAIL('正在播放歌曲与第一首歌曲的歌曲名不相同，点击播放全部按钮来播放歌曲的功能损坏')
            flag = 1

        if flag == 1:
            return 2

        return 0





