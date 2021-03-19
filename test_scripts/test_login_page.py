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
        self.driver = DriverBase(driver='Chrome', enable_headless=False, enable_no_picture=False)

    def teardown_class(self):
        """测试类加载后，执行一次"""
        self.driver.quit_browser()

    @allure.story('登陆界面测试')
    @pytest.mark.parametrize('username,password', test_data)
    def test_login(self, username, password):
        self.driver.open_windows(url=self.URL)
        time.sleep(1)

        self.driver.send_keys(locator=self.USERNAME_INPUT, value=username)
        time.sleep(1)
        self.driver.send_keys(locator=self.PASSWORD_INPUT, value=password, directly_enter=True)
        time.sleep(1)
