# -*- coding:utf-8 -*-
"""
管理登陆页面的所有元素
"""

from selenium.webdriver.common.by import By


class LoginPage(object):

    URL = 'https://www.zhihu.com/'

    # 密码登陆位置
    LOGIN_POSITION = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[1]/div[2]')

    # 用户名、密码、登陆按钮
    USERNAME_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[2]/div/label/input')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[3]/div/label/input')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/div/form/button')
