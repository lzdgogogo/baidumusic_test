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
            log_utils.F_FAIL('测试完成，榜单的播放功能有问题！测试不通过')
        elif tmp == 2:
            log_utils.F_FAIL('测试未完成，原因是等待某控件失败')
        elif tmp == 3:
            log_utils.F_FAIL('测试未完成，原因是获取某歌曲名失败')