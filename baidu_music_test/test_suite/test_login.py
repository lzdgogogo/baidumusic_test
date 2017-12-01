from baidu_music_test.test_case.login_case import login_case
from baidu_music_test.utils import log_utils
# -*- coding:utf-8 -*-
class test_login(login_case):
    def __init__(self):
        super().__init__()

    def login_test01(self):
        """功能：
                太合登录，正常情况，输入正确的账号密码
            返回值：
                1：登录成功
                0：登录失败"""

        log_utils.C_INFO('开始测试登录功能')
        self.after_login()
        if self.taihe_login(1) == 1:
            log_utils.P_PASS('登录成功！测试通过')
            return 1
        else:
            log_utils.F_FAIL('登录失败！测试失败')
            return 0

    def login_test02(self):
        """功能：
                太合登录，异常情况，输入错误的密码
            注意：
                假如输入密码错误次数到3次时，会开始弹出验证码，导致无法继续测试。"""

        log_utils.C_INFO('开始测试登录的异常情况，输入错误的密码')
        self.after_login()

        if self.taihe_login(2) == 0:
            log_utils.P_PASS('登录失败！测试通过！')
            return 1
        else:
            log_utils.F_FAIL('异常情况！测试失败！')
