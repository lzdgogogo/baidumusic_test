#encoding:utf8
from selenium.webdriver.common.by import By
from baidu_music_test.utils import log_utils
from baidu_music_test.page_info.page_base import page_base
#例如在点击退出登录、删除歌单时，弹出的窗口

class dialog_page(page_base):

        yes_button_id = 'com.ting.mp3.android:id/dialog_common_confirm'
        cancel_button_id = 'com.ting.mp3.android:id/dialog_common_cancel'


        def click_yes_button(self):
                """点击确定（此按钮一直在右边）"""
                if self.find_element_by_mode_click(By.ID,self.yes_button_id) == 0:
                    log_utils.F_FAIL('点击确定按钮失败')
                    return 0

        def click_cancel_button(self):
                """点击取消（此按钮在左边）"""
                if self.find_element_by_mode_click(By.ID,self.cancel_button_id) == 0:
                    log_utils.F_FAIL('点击取消按钮失败')
                    return 0

