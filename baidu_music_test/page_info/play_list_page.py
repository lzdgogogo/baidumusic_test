# -*- coding:utf-8 -*-
#此页面是歌单页面
from selenium.webdriver.common.by import By
from baidu_music_test.utils import log_utils
from baidu_music_test.utils.base_utils import base_utils


class play_list_page(base_utils):
    play_list_page_play_list_name_id = 'com.ting.mp3.android:id/tv_playlist_name'           #歌单名
    play_list_page_favorite_button_id = 'com.ting.mp3.android:id/favorite_playlist_layout'  #收藏按钮
    play_list_page_play_all_button_id = 'com.ting.mp3.android:id/random_play'               #播放全部按钮
    play_list_page_download_button_id = 'com.ting.mp3.android:id/header_batch_download'     #缓存按钮
    play_list_page_share_button_id = 'com.ting.mp3.android:id/share_btn'                    #分享按钮
    play_list_page_more_button_id = 'com.ting.mp3.android:id/more_menu'                     #更多按钮（页面最上方的）
    play_list_page_comment_button_id = 'com.ting.mp3.android:id/comment_playlist_layout'    #评论按钮

    play_list_page_first_song_name_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/view_listview\"]\
            /android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]\
            /android.widget.LinearLayout[1]/android.widget.TextView[1]"                     #第一首歌曲的歌曲名
    play_list_page_second_song_name_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/view_listview\"]\
            /android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]\
            /android.widget.LinearLayout[1]/android.widget.TextView[1]"                     #第二首歌曲的歌曲名
    play_list_page_third_song_name_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/view_listview\"]\
            /android.widget.RelativeLayout[4]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]\
            /android.widget.LinearLayout[1]/android.widget.TextView[1]"                     #第三首歌曲的歌曲名

    play_list_page_first_song_more_button_xpath = "//android.widget.ListView[@resource-id=\"com.ting.mp3.android:id/view_listview\"]\
            /android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]\
            /android.widget.RelativeLayout[2]/android.widget.ImageView[1]"                  #第一首歌曲的更多按钮

    #***********************************************下面的控件是点击更多按钮会弹出的控件(不是页面上的更多按钮，是点击某首歌曲旁边的更多按钮more)******************************************************************************************
    play_list_page_more_button_next_play_button_xpath = "//android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]"       #下一首播放
    play_list_page_more_button_favorite_button_xpath = "//android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]"        #喜欢按钮
    play_list_page_more_button_download_button_xpath = "//android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]"        #缓存按钮
    play_list_page_more_button_share_button_xpath = "//android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]"           #分享按钮
    play_list_page_more_button_add_to_button_xpath = "//android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]"          #添加到按钮
    play_list_page_more_button_mv_button_xpath = "//android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]"              #mv按钮
    #***********************************************minibar***********************************************************************************
    minibar_song_name_id = 'com.ting.mp3.android:id/mb_text_trackname'            #minibar中歌名
    minibar_singer_name_id = 'com.ting.mp3.android:id/mb_text_artist'             #歌手名
    minibar_control_button_id = 'com.ting.mp3.android:id/mb_control'              #播放按钮
    minibar_next_button_id = 'com.ting.mp3.android:id/mb_next'                    #下一首按钮
    minibar_playlist_button_id = 'com.ting.mp3.android:id/mb_list'                #列表按钮
    #***********************************************点击更多里的缓存按钮后弹出的缓存栏**********************************************************************************************
    play_list_page_more_button_download_button_download_button_id = 'com.ting.mp3.android:id/dialog_common_confirm'     #点击更多按钮后点击里面的缓存按钮后弹出的缓存栏的缓存按钮
    #***********************************************下面的控件是点击分享按钮后弹出的分享栏（点击页面上的分享是分享整个歌单，点击歌曲的分享会多一个歌词海报栏）**************************************************************************************************
    play_list_page_more_button_share_button_weixin_share_button_id = 'com.ting.mp3.android:id/weixin'   #微信分享按钮
    play_list_page_more_button_share_button_lyric_poster_id = 'com.ting.mp3.android:id/music_story_label'   #歌词海报栏,注意：点击整个页面上方的分享是没有这个栏的
    #***********************************************点击添加到按钮后弹出的栏********************************************************************************************
    play_list_page_more_add_to_play_list_title_xpath  = "//android.widget.RelativeLayout[@resource-id=\"com.ting.mp3.android:id/dialog_common_title_head_container\"]" #添加到歌单的标题栏
    #***********************************************点击页面上方的三个点按钮，就是更多按钮吧。弹出的举报此歌单栏*****************************************************************************************************************
    play_list_page_more_feedback_play_list_layout_id = 'com.ting.mp3.android:id/feedback_playlist_layout'       #举报此歌单的栏的id

    def click_play_list_page_download_button(self):
        if not self.find_element_and_action(By.ID,self.play_list_page_download_button_id,self.action.click,'缓存按钮') == 0:
            log_utils.F_ERROR('点击失败')
            return 1

    def click_play_list_page_comment_button(self):
        if not self.find_element_and_action(By.ID,self.play_list_page_comment_button_id,self.action.click,'评论按钮') == 0:
            log_utils.F_ERROR('点击失败')
            return 1

    def click_play_list_page_share_button(self):
        if not self.find_element_and_action(By.ID,self.play_list_page_share_button_id,self.action.click,'上方分享按钮') == 0:
            log_utils.F_ERROR('点击失败')
            return 1

    def click_play_list_page_more_button(self):
        if not self.find_element_and_action(By.ID,self.play_list_page_more_button_id,self.action.click,'上方更多按钮') == 0:
            log_utils.F_ERROR('点击失败')
            return 1

    def get_play_list_page_minibar_playing_song_name(self):
        """功能：
                获取minibar中正在播放的歌曲的歌曲名"""
        return self.find_element_and_action(By.ID,self.minibar_song_name_id,self.action.get_text,'minibar正在播放的歌曲名')

    def click_play_list_page_minibar_next_song_button(self):
        if not self.find_element_and_action(By.ID,self.minibar_next_button_id,self.action.click,'minibar的下一曲按钮') == 0:
            log_utils.F_ERROR('点击失败')
            return 1

    def get_play_list_page_name(self):
        return self.find_element_and_action(By.ID,self.play_list_page_play_list_name_id,self.action.get_text,'当前歌单名')

    def get_play_list_page_first_song_name(self):
        return self.find_element_and_action(By.XPATH,self.play_list_page_first_song_name_xpath,self.action.get_text,'第一首歌曲的歌曲名')

    def get_play_list_page_second_song_name(self):
        return self.find_element_and_action(By.XPATH,self.play_list_page_second_song_name_xpath,self.action.get_text,'第二首歌曲的歌曲名')

    def get_play_list_page_third_song_name(self):
        return self.find_element_and_action(By.XPATH,self.play_list_page_third_song_name_xpath,self.action.get_text,'第三首歌曲的歌曲名')

    def click_play_list_page_third_song_to_play(self):
        """点击第三首歌曲条目来播放第三首歌曲"""
        if not self.find_element_and_action(By.XPATH,self.play_list_page_third_song_name_xpath,self.action.click,'第三首歌曲条目') == 0:
            log_utils.F_ERROR('点击失败')
            return 1

    def click_play_list_page_play_all_button(self):
        if not self.find_element_and_action(By.ID,self.play_list_page_play_all_button_id,self.action.click,'播放全部按钮') == 0:
            log_utils.F_ERROR('点击失败')
            return 1

    def click_play_list_page_first_song_more_button(self):
        if not self.find_element_and_action(By.XPATH,self.play_list_page_first_song_more_button_xpath,self.action.click,'第一首歌曲的更多按钮') == 0:
            log_utils.F_ERROR('点击失败')
            return 1

    def click_play_list_page_first_song_more_next_play_button(self):
        if not self.find_element_and_action(By.XPATH,self.play_list_page_more_button_next_play_button_xpath,self.action.click,'更多栏的下一首播放按钮') == 0:
            log_utils.F_ERROR('点击失败')
            return 1

    def click_play_list_page_first_song_more_favorite_button(self):
        if not self.find_element_and_action(By.XPATH,self.play_list_page_more_button_favorite_button_xpath,self.action.click,'更多栏的喜欢按钮') == 0:
            log_utils.F_ERROR('点击失败')
            return 1

    def click_play_list_page_first_song_more_download_button(self):
        if not self.find_element_and_action(By.XPATH,self.play_list_page_more_button_download_button_xpath,self.action.click,'更多栏的缓存按钮') == 0:
            log_utils.F_ERROR('点击失败')
            return 1

    def click_play_list_page_first_song_more_share_button(self):
        if not self.find_element_and_action(By.XPATH,self.play_list_page_more_button_share_button_xpath,self.action.click,'更多栏的分享按钮') == 0:
            log_utils.F_ERROR('点击失败')
            return 1

    def click_play_list_page_first_song_more_add_to_button(self):
        if not self.find_element_and_action(By.XPATH,self.play_list_page_more_button_add_to_button_xpath,self.action.click,'更多栏的添加到按钮') == 0:
            log_utils.F_ERROR('点击失败')
            return 1

    def click_play_list_page_first_song_more_mv_button(self):
        if not self.find_element_and_action(By.XPATH,self.play_list_page_more_button_mv_button_xpath,self.action.click,'更多按钮的mv按钮') == 0:
            log_utils.F_ERROR('点击失败')
            return 1

    def is_more_button_download_button_download_button_display(self):
        """判断点击歌曲旁边的更多后弹出的栏的缓存按钮后，弹出的选择品质栏存不存在"""
        if not self.find_element_and_action(By.ID,self.play_list_page_more_button_download_button_download_button_id,self.action.is_displayed,'选择品质栏') == 0:
            return 1
        return 0

    def is_more_button_share_button_lyric_poster_display(self):
        """判断点击歌曲旁边的更多后弹出的栏的分享按钮后，弹出的分享栏存不存在"""
        if not self.find_element_and_action(By.ID,self.play_list_page_more_button_share_button_lyric_poster_id,self.action.is_displayed,'分享栏')  == 0:
            return 1
        return 0

    def is_more_button_add_to_button_play_list_display(self):
        """判断点击歌曲旁边的更多后弹出的栏的添加到按钮后，弹出的歌单栏存不存在"""
        if not self.find_element_and_action(By.XPATH,self.play_list_page_more_add_to_play_list_title_xpath,self.action.is_displayed,'我的歌单栏') == 0:
            return 1
        return 0
