# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from baidu_music_test.data import base_data
from baidu_music_test.page_info.batch_download_page import batch_download_page
from baidu_music_test.page_info.comment_page import comment_page
from baidu_music_test.page_info.home_page.home_music_page_dependence_page.home_music_play_list_page import home_music_play_list_page
from baidu_music_test.page_info.home_page.home_music_page_dependence_page.play_list_page import play_list_page
from baidu_music_test.page_info.play_page.music_play_page import music_play_page
from baidu_music_test.utils import log_utils
from baidu_music_test.utils import api_utils
from baidu_music_test.page_info import mv_page


class play_list_case(home_music_play_list_page,music_play_page,play_list_page,mv_page.mv_play_page,comment_page,batch_download_page):

    def play_list_play_test(self):
        """功能：
                验证歌单页面相关的播放功能，歌单封面的播放按钮、歌单内部的播放全部按钮，点击歌曲进行播放
            步骤：
                1.进入APP，点击歌单按钮，进入歌单页面,获取第一个歌单的名称
                2.点击第一个歌单页面封面的播放按钮
                3.进入了歌曲播放页，验证是否正在播放，记录下正在播放的歌曲名称
                4.点击歌曲播放页的返回按钮，返回歌单页面，点击第一个歌单的封面进入第一个歌单页面，通过api获取前三首歌曲的歌曲名，跟页面上的歌曲名进行对比
                5.获取第一首歌曲的歌曲名，跟之前的歌曲名比较
                6.获取第三首歌曲的歌曲名，点击第三首歌曲条目，比较歌曲名，查看是否在播放，点击返回
                7.回到歌单页，点击播放全部按钮，比较第一首歌曲的歌曲名，查看是否在播放，点击返回
            返回值：
                0：测试通过
                1：等待某控件超时
                2：测试失败不通过
                3：获取某文本失败
                4：从api获取歌曲名失败"""

        flag = 0
        log_utils.C_INFO('开始测试歌单页面相关的播放功能')

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
        second_song_name = self.get_play_list_page_second_song_name()
        third_song_name = self.get_play_list_page_third_song_name()
        if first_song_name == 1 or first_song_name == 2 or third_song_name == 1 or third_song_name == 2 or second_song_name == 1 or second_song_name==2:
            log_utils.F_ERROR('获取歌曲名失败，无法继续测试')
            return 3
        log_utils.C_INFO('第一首歌曲名为：'+first_song_name)
        log_utils.C_INFO('第二首歌曲名为：'+second_song_name)
        log_utils.C_INFO('第三首歌曲名为：'+third_song_name)

        log_utils.C_STEP('开始从api获取当前歌单的前三首歌曲')
        song_name_list = api_utils.get_first_play_list_first_song_name(3)   #从api获取前三首歌曲名
        if not song_name_list == 1:
            if first_song_name == song_name_list[0] and second_song_name == song_name_list[1] and third_song_name == song_name_list[2]:
                log_utils.C_INFO('从页面上获取的前三首歌曲名信息于从api获取的前三首歌曲名相同')
            else:
                log_utils.F_ERROR('从页面上获取的前三首歌曲名信息于从api获取的前三首歌曲名不相同，请检查相关功能')
                flag = 2

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
        elif flag == 2:
            return 4

        return 0

    def play_list_more_test(self):
        """功能：
            对歌单页面的更多按钮中的各项功能，
            点击缓存按钮后能否弹出到缓存栏，点击喜欢能否收藏歌曲，点击分享是否能弹出分享栏，点击下一首会下一首播放，点击mv会跳转到mv播放页，点击添加到会弹出歌单栏进行测试
        步骤：
            1.点击进入最热歌单页面，跟从api获取的歌单名相对比
            2.点击进入第一个歌单页面，点击播放第三首歌曲，点击返回到歌单页面
            3.点击第一首歌的更多按钮，点击下一首播放按钮，点击minibar中的下一曲按钮，验证歌曲名来验证下一首播放按钮功能
            4.点击第一首歌的更多按钮，点击喜欢按钮，从api验证是否喜欢成功，点击返回按钮
            5.点击第一首歌的更多按钮，点击缓存按钮，检测是否弹出缓存栏，点击返回按钮
            6.点击第一首歌的更多按钮，点击分享按钮，检测是否弹出分享栏，点击返回按钮
            7.点击第一首歌的更多按钮，点击添加到按钮，检测是否弹出歌单栏，点击返回按钮
            8.从api检测第一首歌是否有mv，假如有，点击第一首歌的更多按钮，点击mv按钮，等待是否能进入mv的播放页面
            9.测试完毕，返回flag
        返回值：
            0：测试成功
            1：从api获取的歌单名与从页面提取的歌单名不一致
            2：从api获取的歌名与正在播放的歌曲名不一致，更多--下一首播放按钮功能损坏
            3：从api获取数据失败
            4：某控件不存在
            5：歌曲没有mv，这个点无法测试
            6：收藏不成功
            7：从界面获取歌单名失败
            8：进入歌单页面超时"""

        flag = 0
        log_utils.C_INFO('开始测试歌单页面更多按钮中的各项功能，点击缓存、评论是否能跳转到对应页面，点击分享、举报能否弹出对应栏')

        self.click_play_list_button()
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.play_list_page_newest_button_id,'进入歌单页面') == 1:
            return 8

        first_play_list_name = self.get_play_list_page_first_play_list_name()
        if first_play_list_name == 1 or first_play_list_name == 2:
            log_utils.F_ERROR('从界面获取歌单名失败')
            flag = 7
        log_utils.C_STEP('第一个歌单名为：'+first_play_list_name)
        log_utils.C_STEP('开始从api获取最热歌单的第一个歌单名')
        list_name = api_utils.get_first_play_list_name()
        log_utils.C_INFO('获取到的歌单名为：'+list_name)
        if not list_name == 1:
            if not list_name == first_play_list_name:
                log_utils.F_ERROR('从api获取的歌单名与从页面提取的歌单名不一致！')
                self.screenshot('从api获取的歌单名与从页面提取的歌单名不一致，从api获取的歌单名为：'+list_name)
                flag = 1
            else:
                log_utils.C_INFO('从api获取的歌单名与从页面提取的歌单名一致')
        else:
            flag = 3

        self.click_play_list_page_first_play_list()
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.play_list_page_play_all_button_id,'进入第一个歌单页') == 1:
            return 1
        self.my_sleep(2)
        self.click_play_list_page_third_song_to_play()
        self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.music_play_page_song_name_text_id,'进入歌曲播放页')
        self.click_music_play_page_back_button()
        self.my_sleep(3)

        self.click_play_list_page_first_song_more_button()  #点击第一首歌曲的更多按钮
        self.my_sleep(3)
        self.click_play_list_page_first_song_more_next_play_button()    #点击下一首播放
        self.my_sleep(2)
        self.click_play_list_page_minibar_next_song_button()
        self.my_sleep(2)
        playing_song_name = self.get_play_list_page_minibar_playing_song_name()
        log_utils.C_INFO('当前正在播放歌曲名为：'+playing_song_name)

        log_utils.C_STEP('从api获取歌曲名')
        song_name_list = api_utils.get_first_play_list_first_song_name(3)
        if not song_name_list == 1:
            log_utils.C_INFO('获取到的第一首歌曲名为：'+song_name_list[0])
            if not playing_song_name == song_name_list[0]:
                log_utils.F_ERROR('从api获取的歌名与从页面提取的正在播放歌曲名不一致！')
                self.screenshot('从api获取的歌名与从页面提取的正在播放歌曲名不一致，从api获取的歌名为：'+song_name_list[0])
                flag = 2
            else:
                log_utils.C_INFO('从api获取的歌名与从页面提取的正在播放歌曲名一致，更多--下一首播放功能完好')
        else:
            flag = 3

        log_utils.C_STEP('开始测试点击喜欢按钮能否喜欢')
        self.my_sleep(2)
        self.click_play_list_page_first_song_more_button()
        self.my_sleep()
        self.click_play_list_page_first_song_more_favorite_button()
        self.my_sleep(3)
        log_utils.C_STEP('开始从api获取用户收藏的信息')
        collect_song_name_list = api_utils.get_user_collect_song_list()
        if collect_song_name_list == 1:
            flag = 3
        else:
            log_utils.C_INFO('从api获取的用户收藏的第一首歌名为：'+collect_song_name_list[0])
            if collect_song_name_list[0] == song_name_list[0]:
                log_utils.C_INFO('用户收藏的第一首歌曲名与本歌单第一首歌曲名相同，收藏成功')
            else:
                log_utils.C_INFO('用户收藏的第一首歌曲名与本歌单第一首歌曲名不相同，收藏不成功')
                flag = 6
        self.my_sleep(2)
        self.click_play_list_page_first_song_more_button()
        self.my_sleep()
        self.click_play_list_page_first_song_more_favorite_button()

        log_utils.C_STEP('开始检查点击缓存按钮能否弹出缓存栏')
        self.my_sleep(2)
        self.click_play_list_page_first_song_more_button()
        self.my_sleep()
        self.click_play_list_page_first_song_more_download_button()
        self.my_sleep(3)
        if self.is_more_button_download_button_download_button_display() == 1:          #检测缓存栏是否弹出
            flag = 4
            log_utils.F_ERROR('缓存栏没有弹出')
        self.driver.press_keycode(4)    #点击返回键

        log_utils.C_STEP('开始测试点击分享按钮能否弹出分享栏')
        self.my_sleep(2)
        self.click_play_list_page_first_song_more_button()
        self.my_sleep(2)
        self.click_play_list_page_first_song_more_share_button()
        self.my_sleep(2)
        if self.is_more_button_share_button_lyric_poster_display() == 1:            #检查分享栏是否弹出
            flag = 4
            log_utils.F_ERROR('分享栏没有弹出')
        self.driver.press_keycode(4)
        self.my_sleep(2)

        self.click_play_list_page_first_song_more_button()
        self.my_sleep(2)
        self.click_play_list_page_first_song_more_add_to_button()
        self.my_sleep(2)
        if self.is_more_button_add_to_button_play_list_display() == 1:                  #检测歌单栏是否弹出
            flag = 4
            log_utils.F_ERROR('歌单栏没有弹出')
        self.driver.press_keycode(4)
        self.my_sleep(2)

        log_utils.C_INFO('从api获取has_mv的信息来判断第一首歌曲是否有mv')
        has_mv_code = api_utils.get_first_play_list_first_song_have_mv()    #先检查该歌曲是否有mv，假如有点击之后检测是否跳转到mv页面
        if has_mv_code == '1':
            log_utils.C_STEP('第一首歌曲有mv，开始验证点击mv按钮能否跳转到mv页面')
            self.click_play_list_page_first_song_more_button()
            self.my_sleep(2)
            self.click_play_list_page_first_song_more_mv_button()
            self.wait_element_by_mode(base_data.wait_time_mid,By.ID,mv_page.mv_play_page.mv_play_box_id,'进入mv播放页')
            log_utils.F_ERROR('成功进入mv播放页')
        elif has_mv_code == '0':
            log_utils.F_ERROR('第一首歌曲没有mv，无法测试跳转到mv页面')
            flag = 5
        else:
            flag = 3

        return flag

    def play_list_top_button_test(self):
        """对歌单页面上方的控件进行测试，主要是点击后有没有对应的边栏弹出，和会不会跳转到对应的页面
        返回值：
            1：进入歌单页面超时
            2：进入评论页面失败
            3：获取评论页的标题失败
            4：等待举报栏失败
            5：等待分享栏失败
            6：进入批量缓存页失败"""
        flag = 0
        log_utils.C_INFO('开始测试歌单页面更多按钮中的各项功能，点击缓存、评论是否能跳转到对应页面，点击分享、举报能否弹出对应栏')

        self.click_play_list_button()
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.play_list_page_newest_button_id,'进入歌单页面') == 1:
            return 1

        self.click_play_list_page_first_play_list()
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,self.play_list_page_play_all_button_id,'进入第一个歌单页') == 1:
            return 1

        log_utils.C_STEP('开始测试点击评论按钮能否跳转到评论页面')
        play_list_page.click_play_list_page_comment_button(self)
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,comment_page.comment_page_title_bar_title_id,'进入评论页面') == 1:
            flag = 2
        else:
            title = comment_page.get_comment_page_title_bar_title_text(self)
            if title == 1:
                flag = 3
            else:
                log_utils.C_INFO('当前评论页面的标题为：'+title)
            comment_page.click_comment_page_title_bar_back_button(self)


        self.my_sleep(3)
        log_utils.C_STEP('开始测试点击页面上方更多按钮，是否会弹出举报栏')
        play_list_page.click_play_list_page_more_button(self)
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,play_list_page.play_list_page_more_feedback_play_list_layout_id,'下方举报栏弹出') == 1:
            flag = 4
        else:
            log_utils.C_INFO('举报栏出现，点击更多按钮功能有效')
            self.driver.press_keycode(4)
        self.my_sleep(3)

        log_utils.C_STEP('开始测试点击页面上方分享按钮，是否会弹出分享栏')
        play_list_page.click_play_list_page_share_button(self)
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,play_list_page.play_list_page_more_button_share_button_weixin_share_button_id,'下方分享栏弹出') == 1:
            flag = 5
        else:
            log_utils.C_INFO('分享栏出现，点击分享按钮有效')
            self.driver.press_keycode(4)
        self.my_sleep(3)

        log_utils.C_STEP('开始测试点击缓存按钮会不会跳转到缓存页')
        play_list_page.click_play_list_page_download_button(self)
        if self.wait_element_by_mode(base_data.wait_time_mid,By.ID,batch_download_page.batch_download_page_download_layout_button_id,'进入批量缓存页面') == 1:
            flag = 6
        else:
            log_utils.C_INFO('进入批量缓存页，点击批量缓存按钮功能成功')

        return flag