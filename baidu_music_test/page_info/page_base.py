__author__ = '刘子恒'
#所有页面的基类，包括所有页面的公共方法。


class page_base(object):
    def __init__(self,driver):
        """注意：
                一定要传入self.driver"""
        self.driver=driver

    def find_element_by_mode_click(self,mode,element=''):
        """功能：
                以某种方式查找并点击某控件
            参数：
                mode：查找的方式，例如：By.ID，By.XPATH。
                element：查找控件的依据，比如id，xpath，这个方式必须跟前面的方式对应。
            返回值：
                1：点击正常完成
                0：没有点击成功，已经抛出异常"""
        try:
            self.driver.find_element(mode,element).click()
            return 1
        except:
            return 0

    def find_element_by_mode_is_displayed(self,mode,element=''):
        """功能：
                以某种方式查找某控件是否显示
            参数：
                mode：查找的方式，例如：By.ID，By.XPATH。
                element：查找控件的依据，比如id，xpath，这个方式必须跟前面的方式对应。
            返回值：
                1：正常显示
                0：没有找到该控件，已经抛出异常
                -1：没有显示"""
        try:
            if self.driver.find_element(mode,element).is_displayed():
                return 1
            else:
                return -1
        except:
            return 0

    def find_element_by_mode_send_keys(self,mode,element='',keys=''):
        """功能：
                以某种方式查找某控件,并且输入keys
            参数：
                mode：查找的方式，例如：By.ID，By.XPATH。
                element：查找控件的依据，比如id，xpath，这个方式必须跟前面的方式对应。
                keys：要输入的字符串
            返回值：
                1：正常输入
                0：没有找到该控件，已经抛出异常
                """
        try:
            self.driver.find_element(mode,element).send_keys(keys)
            return 1
        except:
            return 0