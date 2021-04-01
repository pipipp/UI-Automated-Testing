# -*- coding:utf-8 -*-
import os
import time
import allure
import pytest

from utils.drivers import DriverBase
from utils.tools import get_yaml_test_data
from utils.decorators import error_screenshot
from pages.login_page import LoginPage
from settings import MODULE_DIR


# 获取测试数据
test_data = get_yaml_test_data(os.path.join(MODULE_DIR['test_data_dir'], 'login_page.yaml'))


@allure.story('浏览器驱动初始化')
@pytest.fixture(scope='session')
def browser():
    """加载浏览器驱动"""
    driver = DriverBase(driver='Chrome', enable_headless=False, enable_no_picture=False)
    yield driver
    driver.quit_browser()


@allure.feature('知乎登陆功能')
class TestLoginPage(LoginPage):

    @allure.story('登陆界面测试')
    @error_screenshot()
    @pytest.mark.parametrize('username,password', test_data)
    def test_login(self, env, username, password, browser):
        browser.open_windows(url=env['host'] + self.URL)

        browser.click_button(self.LOGIN_POSITION)
        browser.send_keys(locator=self.USERNAME_INPUT, value=username)
        browser.send_keys(locator=self.PASSWORD_INPUT, value=password)
        browser.click_button(self.LOGIN_BUTTON)
