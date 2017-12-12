# -*- coding:utf-8 -*-
from baidu_music_test.test_case.music_play_page_case import music_play_page_case
from baidu_music_test.utils import log_utils


class music_play_page_test(music_play_page_case):
    def music_play_page_test_01(self):
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

