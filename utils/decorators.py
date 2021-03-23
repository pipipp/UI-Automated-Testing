# -*- coding:utf-8 -*-
"""
装饰器模块
"""

import os
import datetime
import functools

from utils.loggers import LOGGER
from settings import MODULE_DIR


# 失败截图装饰器
def error_screenshot():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            browser_driver = kwargs.get('browser')  # 获取driver
            func_name = func.__name__  # 获取测试函数名

            start_time = datetime.datetime.now()
            LOGGER.debug(f'用例（{func_name}）执行时间：{start_time}')

            try:
                func(*args, **kwargs)  # 执行测试函数
            except Exception as ex:
                LOGGER.error(f'用例（{func_name}）执行失败，错误信息：{ex}')
                # 截图保存
                browser_driver.screenshot(storage_path=MODULE_DIR['failure_screenshot'],
                                          picture_name=func_name)

            end_time = datetime.datetime.now()
            LOGGER.debug(f'用例（{func_name}）结束时间：{start_time}，耗时：{(end_time - start_time).total_seconds()}s')
        return wrapper
    return decorator
