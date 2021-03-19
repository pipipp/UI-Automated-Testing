# -*- coding:utf-8 -*-
"""
Allure报告模块
"""

import allure


def add_common_report(case, http, expected):
    """
    添加常用报告信息
    :param case: 测试用例名称
    :param http: 请求对象
    :param expected: 预期结果
    :return:
    """
    with allure.step('测试用例名称'):
        allure.attach(case, 'case')

    with allure.step('请求对象'):
        allure.attach(http['path'], 'path')
        allure.attach(http['method'], 'method')

        with allure.step('headers'):
            keys = http['headers'].keys()
            values = http['headers'].values()
            for k, v in zip(keys, values):
                allure.attach(v, k)

        with allure.step('params'):
            keys = http['params'].keys()
            values = http['params'].values()
            for k, v in zip(keys, values):
                allure.attach(v, k)

    with allure.step('预期结果'):
        keys = expected['response'].keys()
        values = expected['response'].values()
        for k, v in zip(keys, values):
            allure.attach(str(v), k)
