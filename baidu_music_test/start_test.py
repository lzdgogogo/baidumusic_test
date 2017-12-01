from baidu_music_test.test_suite.play_list_test import play_list_test
from baidu_music_test.test_suite.test_login import test_login
from baidu_music_test.test_suite.song_list_test import song_list_test
# -*- coding:utf-8 -*-


class run_case(play_list_test):
    def run_test(self):

        self.wait_start_app()

        # self.login_test02()
        # self.reset_app()
        # self.login_test01()

        self.play_list_test01()


        self.tear_down()



if __name__ == '__main__':
    test = run_case()

    test.run_test()




