# -*- coding:utf-8 -*-
"""
管理登陆页面的所有元素
"""

from selenium.webdriver.common.by import By


class LoginPage(object):

    URL = 'https://www.zhihu.com/'

    USERNAME_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[1]/div[2]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[2]/div/label/input')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/div/form/button')
