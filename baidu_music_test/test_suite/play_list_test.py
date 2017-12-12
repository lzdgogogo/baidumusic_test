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
        elif tmp == 4:
            log_utils.F_FAIL('测试失败，原因：从api获取歌曲名信息失败')

    def play_list_test02(self):
        tmp = self.play_list_more_test()
        if tmp == 0:
            log_utils.P_PASS('测试通过，歌单页面的歌曲条目的更多按钮中各项功能完好。包括下一首，喜欢，添加到，缓存，分享，mv按钮的点击弹出对应下边栏，喜欢能否真正收藏的功能。')
        elif tmp == 1:
            log_utils.F_FAIL('测试失败，原因：从api获取的歌单名与从页面提取的歌单名不一致')
        elif tmp == 2:
            log_utils.F_FAIL('测试失败，原因：从api获取的歌名与正在播放的歌曲名不一致，更多--下一首播放按钮功能损坏')
        elif tmp == 3:
            log_utils.F_FAIL('测试失败，原因：从api获取数据失败')
        elif tmp == 4:
            log_utils.F_FAIL('测试失败，原因：某控件不存在')
        elif tmp == 5:
            log_utils.F_FAIL('测试失败，原因：歌曲没有mv，这个点无法测试')
        elif tmp == 6:
            log_utils.F_FAIL('测试失败，原因：收藏不成功')
        elif tmp == 7:
            log_utils.F_FAIL('测试失败，原因：从界面获取歌单名失败')
        elif tmp == 8:
            log_utils.F_FAIL('测试失败，原因：进入歌单页面超时')

    def play_list_test_03(self):
        tmp = self.play_list_top_button_test()
        if tmp == 0:
            log_utils.P_PASS('测试通过，歌单页面上方的控件（分享、更多、批量缓存）功能完好，包括点击控件后有没有对应的边栏弹出，或会不会跳转到对应的页面')
        elif tmp == 1:
            log_utils.F_FAIL('测试失败，原因：进入歌单页面超时')
        elif tmp == 2:
            log_utils.F_FAIL('测试失败，原因：进入评论页面失败')
        elif tmp == 3:
            log_utils.F_FAIL('测试失败，原因：获取评论页的标题失败')
        elif tmp == 4:
            log_utils.F_FAIL('测试失败，原因：等待举报栏失败')
        elif tmp == 5:
            log_utils.F_FAIL('测试失败，原因：等待分享栏失败')
        elif tmp == 6:
            log_utils.F_FAIL('测试失败，原因：进入批量缓存页失败')

