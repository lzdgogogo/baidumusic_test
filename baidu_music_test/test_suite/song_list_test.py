# -*- coding:utf-8 -*-
from baidu_music_test.test_case.song_list_case import song_list_case
from baidu_music_test.utils import log_utils
#榜单的测试

class song_list_test(song_list_case):
    def song_list_test01(self):
        tmp = self.song_list_play_test()
        if tmp == 0:
            log_utils.P_PASS('测试完成，榜单的各项播放功能正常！测试通过')
        elif tmp == 1:
            log_utils.F_FAIL('测试失败，榜单的播放功能有问题！')
        elif tmp == 2:
            log_utils.F_FAIL('测试失败，原因：等待某控件失败')
        elif tmp == 3:
            log_utils.F_FAIL('测试失败，原因：获取某歌曲名失败')
        elif tmp == 4:
            log_utils.F_FAIL('测试失败，原因：从api获取歌曲名失败')