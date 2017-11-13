#encoding:utf8
from selenium.webdriver.common.by import By
from baidu_music_test.utils import log_utils
#例如在点击退出登录、删除歌单时，弹出的窗口
from baidu_music_test.utils.base_utils import base_utils


class dialog_page(base_utils):
        def __init__(self):
            super().__init__()

        yes_button_id = 'com.ting.mp3.android:id/dialog_common_confirm'
        cancel_button_id = 'com.ting.mp3.android:id/dialog_common_cancel'


        def click_yes_button(self):
                """点击确定（此按钮一直在右边）"""
                if not self.find_element_and_action(By.ID,self.yes_button_id,'click','确定按钮') == 0:
                    log_utils.F_FAIL('点击确定按钮失败')
                    return 1

        def click_cancel_button(self):
                """点击取消（此按钮在左边）"""
                if not self.find_element_and_action(By.ID,self.cancel_button_id,'click','取消按钮') == 0:
                    log_utils.F_FAIL('点击取消按钮失败')
                    return 1

