__author__ = '刘子恒'

from baidu_music_test.testCase.test_login import login_test

class run_test(login_test):
    def run_test(self):

        self.wait_start_app()

        self.login_test02()
        self.reset_app()
        self.login_test01()



        self.tear_down()



if __name__ == '__main__':
    test = run_test()

    test.run_test()




