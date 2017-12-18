# -*- coding:utf-8 -*-
from baidu_music_test.test_case.music_play_page_case import music_play_page_case
from baidu_music_test.utils import log_utils


class music_play_page_test(music_play_page_case):
    def music_play_page_test_01(self):
        """测试歌曲播放页的UI展示"""
        tmp = self.music_play_page_UI_test()
        if tmp == 0:
            log_utils.P_PASS('测试通过，UI展示：歌曲播放页的各项展示功能，依次是专辑图、返回按钮、播放次数、当前播放时间、总时长、歌曲名、歌手名、歌词按钮、\
缓存按钮、喜欢按钮、分享按钮、更多按钮、播放模式按钮、上一曲按钮、播放暂停按钮、下一曲按钮、播放列表按钮、相关明星、相似歌曲、推荐歌单、精彩热评。')
        elif tmp == 1:
            log_utils.F_FAIL('测试失败，原因：进入歌单页面失败')
        elif tmp == 2:
            log_utils.F_FAIL('测试失败，原因：进入歌曲播放页失败')
        elif tmp == 3:
            log_utils.F_FAIL('测试失败，原因：某控件显示错误')

    def music_play_page_test_02(self):
        """测试点击专辑图会不会进入歌词页，点击歌词按钮会不会进入歌词页"""
        tmp = self.music_play_page_album_test()
        if tmp == 0:
            log_utils.P_PASS('测试通过，点击专辑图不会进入歌词页，点击歌词按钮进入歌词页')
        elif tmp == 1:
            log_utils.F_FAIL('测试失败，原因：进入歌单页面失败')
        elif tmp == 2:
            log_utils.F_FAIL('测试失败，原因：进入歌曲播放页失败')
        elif tmp == 3:
            log_utils.F_FAIL('测试失败，原因：点击专辑图进入了歌词页面（不应该进入）')
        elif tmp == 4:
            log_utils.F_FAIL('测试失败，原因：点击了歌词按钮没有进入歌词页面')

    def music_play_page_test_03(self):
        """测试点击各个入口（今日推荐、歌单、榜单、最近播放）能否正常进入歌曲播放页"""
        tmp = self.click_entrance_can_go_to_music_play_page_test()
        if tmp == 0:
            log_utils.P_PASS('测试通过，点击各个入口（今日推荐、歌单、榜单、最近播放）可以正常进入歌曲播放页')
        elif tmp == 1:
            log_utils.F_FAIL('测试失败，原因：进入今日推荐页超时')
        elif tmp == 2:
            log_utils.F_FAIL('测试失败，原因：进入歌曲播放页失败')
        elif tmp == 3:
            log_utils.F_FAIL('测试失败，原因：进入歌单页超时')
        elif tmp == 4:
            log_utils.F_FAIL('测试失败，原因：进入第一个歌单页面超时')
        elif tmp == 5:
            log_utils.F_FAIL('测试失败，原因：进入榜单页面超时')
        elif tmp == 6:
            log_utils.F_FAIL('测试失败，原因：进入第一个榜单页面超时')
        elif tmp == 7:
            log_utils.F_FAIL('测试失败，原因：进入我的页面超时')
        elif tmp == 8:
            log_utils.F_FAIL('测试失败，原因：进入最近播放页超时')

    def music_play_page_test_04(self):
        tmp = self.music_play_page_progress_bar_display()
        if tmp == 0:
            log_utils.P_PASS('测试通过，在播放的情况下拖动进度条成功')
        elif tmp == 1:
            log_utils.F_FAIL('测试失败，原因：进入今日推荐页失败')
        elif tmp == 2:
            log_utils.F_FAIL('测试失败，原因：进入歌曲播放页失败')

    def music_play_page_test_05(self):
        tmp = self.music_play_page_progress_bar_pause_displayed()
        if tmp == 0:
            log_utils.P_PASS('测试通过，在暂停的情况下拖动进度条成功，且拖动完进度条歌曲开始播放')
        elif tmp == 1:
            log_utils.F_FAIL('测试失败，原因：进入今日推荐页失败')
        elif tmp == 2:
            log_utils.F_FAIL('测试失败，原因：进入歌曲播放页失败')
