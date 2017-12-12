# -*- coding:utf-8 -*-
#mv的播放页
from selenium.webdriver.common.by import By
from baidu_music_test.utils.base_utils import base_utils


class mv_play_page(base_utils):
    mv_play_box_id = 'com.ting.mp3.android:id/app_video_box'        #播放框

    def is_mv_play_box_displayed(self):
        """检查mv播放框
        返回值：
            1：不存在
            0：存在"""
        if not self.find_element_and_action(By.ID,self.mv_play_box_id,self.action.is_displayed,'mv播放框') == 0:
            return 1
        return 0
