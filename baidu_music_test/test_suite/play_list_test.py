# -*- coding:utf-8 -*-
#歌单的测试
from baidu_music_test.test_case.play_list_case import play_list_case
from baidu_music_test.utils import log_utils


class play_list_test(play_list_case):
    def __init__(self):
        super().__init__()

    def play_list_test01(self):
        tmp = self.play_list_play_test()
        if tmp == 0:
            log_utils.P_PASS('测试通过，歌单页面的播放功能完好，包括歌单封面的播放按钮，点击歌曲条目进行播放，点击歌单页面的播放全部按钮来播放。')
        elif tmp == 1:
            log_utils.F_FAIL('测试失败，原因：等待某控件超时！')
        elif tmp == 2:
            log_utils.F_FAIL('测试失败，原因：某播放功能损坏！')
        elif tmp == 3:
            log_utils.F_FAIL('测试失败，原因：获取某文本失败！')


