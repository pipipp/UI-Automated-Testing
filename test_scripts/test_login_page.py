# -*- coding:utf-8 -*-
import os
import time
import allure
import pytest

from utils.drivers import DriverBase
from pages.login_page import LoginPage
from utils.tools import get_yaml_test_data
from settings import MODULE_DIR


# 获取测试数据
test_data = get_yaml_test_data(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))


@allure.feature('知乎登陆功能')
class TestLoginPage(LoginPage):

    def setup_class(self):
        """测试类加载前，执行一次"""
        self.browser = DriverBase(driver='Chrome', enable_headless=False, enable_no_picture=False)

    def teardown_class(self):
        """测试类加载后，执行一次"""
        self.browser.quit_browser()

    def setup(self):
        """每个测试方法运行前，执行一次"""
        pass

    def teardown(self):
        """每个测试方法运行后，执行一次"""
        pass

    @allure.story('登陆界面测试')
    @pytest.mark.parametrize('username,password', test_data)
    def test_login(self, username, password):
        self.browser.open_windows(url=self.URL)

        self.browser.click_button(self.LOGIN_POSITION)

        self.browser.send_keys(locator=self.USERNAME_INPUT, value=username)
        self.browser.send_keys(locator=self.PASSWORD_INPUT, value=password)
        self.browser.click_button(self.LOGIN_BUTTON)

        self.browser.screen_shot(storage_path=MODULE_DIR['failure_screenshot'], picture_name='Demo')
