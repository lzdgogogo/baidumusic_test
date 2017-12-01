from baidu_music_test.utils.base_utils import base_utils
# -*- coding:utf-8 -*-

#主页--随心听页面

class home_anylisten_page(base_utils):
    def __init__(self):
        super().__init__()

    on_the_way_xpath = "//android.widget.LinearLayout[@resource-id=\"com.ting.mp3.android:id/scene_container\"]\
                        /android.widget.FrameLayout[1]"             #在路上布局
    working_xpath = "//android.widget.LinearLayout[@resource-id=\"com.ting.mp3.android:id/scene_container\"]\
                        /android.widget.FrameLayout[2]"             #工作布局
    sport_xpath = "//android.widget.LinearLayout[@resource-id=\"com.ting.mp3.android:id/scene_container\"]\
                        /android.widget.FrameLayout[3]"             #运动布局
    goodnight_xpath = "//android.widget.LinearLayout[@resource-id=\"com.ting.mp3.android:id/scene_container\"]\
                        /android.widget.FrameLayout[4]"             #晚安布局
    fifteen_min_id = 'com.ting.mp3.android:id/img_time_fm_15min'    #15min


