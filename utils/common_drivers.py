# -*- coding:utf-8 -*-
"""
封装各种公共的业务功能方法
"""

from utils.driver_base import DriverBase


class Drivers(DriverBase):

    def __init__(self, driver='Chrome', enable_headless=False, enable_no_picture=False, enable_maximize_window=False):
        super(Drivers, self).__init__(driver, enable_headless, enable_no_picture, enable_maximize_window)

    def login_interface(self, url, login_button, login_position=None, username={}, password={}):
        """
        进入登陆界面，模拟登陆
        :param url: Login URL
        :param login_button: 登陆按钮locator
        :param login_position: 进行登陆的页面位置（如果需要切换的话）
        :param username: 用户名，字典格式：{'locator': '//', 'value': 'abc'}
        :param password: 密码，字典格式：{'locator': '//', 'value': '456'}
        :return:
        """
        self.open_windows(url=url)

        if login_position:  # 有些页面要切换到指定地方，才能进行登陆
            self.click_button(locator=login_position)

        self.send_keys(locator=username['locator'], value=username['value'])
        self.send_keys(locator=password['locator'], value=password['value'])
        self.click_button(login_button)
