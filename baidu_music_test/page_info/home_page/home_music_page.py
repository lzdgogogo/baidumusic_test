from baidu_music_test.page_info.home_page.home_page import home_page

__author__ = '刘子恒'

#百度音乐app的首页，首页的音乐分栏

class home_music_page(home_page):
        def __init__(self):
            super().__init__()

        #上边栏
        search_layout_id='com.ting.mp3.android:id/search_layout'                                                        #搜索栏
        #搜索栏下方边栏
        recommend_xpath="//android.widget.HorizontalScrollView[@resource-id=\"com.ting.mp3.android:id/tabsLayout\"]\
                        /android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]"      #搜索栏下方推荐按钮
        song_list_xpath="//android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]"       #歌单按钮

