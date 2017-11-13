from baidu_music_test.test_suite.test_login import test_login

__author__ = '刘子恒'


class run_case(test_login):
    def run_test(self):

        self.wait_start_app()

        self.login_test02()
        self.reset_app()
        self.login_test01()


        self.tear_down()



if __name__ == '__main__':
    test = run_case()

    test.run_test()




