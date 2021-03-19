# -*- coding:utf-8 -*-
"""
这个文件会在整个测试完成后被调用
"""


def pytest_sessionfinish(session):
    """
    生成environment.properties文件，可以在报告上的overview页面上的ENVIRONMENT位置展示信息
    :param session:
    :return:
    """
    with open("{}/allure-results/environment.properties".format(session.config.rootdir), "w") as f:
        f.write("env=test\nbrowser=Chrome\ndomain=https://www.zhihu.com/")
