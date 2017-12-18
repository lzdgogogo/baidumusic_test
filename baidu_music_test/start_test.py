# -*- coding:utf-8 -*-
from baidu_music_test.test_suite.music_play_page_test import music_play_page_test
from baidu_music_test.test_suite.play_list_test import play_list_test
from baidu_music_test.test_suite.test_login import test_login
from baidu_music_test.test_suite.song_list_test import song_list_test



class run_case(music_play_page_test):
        def run_test(self):

                self.wait_start_app()

                music_play_page_test.music_play_page_test_05(self)

                self.tear_down()



if __name__ == '__main__':
        test = run_case()

        test.run_test()




