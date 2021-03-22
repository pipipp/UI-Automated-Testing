# -*- coding:utf-8 -*-
"""
装饰器模块
"""

import os
import datetime

from utils.loggers import LOGGER
from settings import MODULE_DIR


# 失败截图装饰器
def error_screenshot(driver):  # driver为浏览器对象
    def decorator(func):  # func为被装饰的函数
        def wrapper(*args, **kwargs):  # 被装饰函数的实参
            func_name = func.__name__
            start_time = datetime.datetime.now()
            LOGGER.debug(f'用例（{func_name}）执行时间：{start_time}')

            try:
                func(*args, **kwargs)  # 执行被装饰函数
            except Exception as ex:
                LOGGER.error(f'用例（{func_name}）执行失败，错误信息：{ex}')

                current_times = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                storage = os.path.join(MODULE_DIR['failure_screenshot'], f'{current_times}_{func.__name__}.jpg')

                driver.driver.save_screenshot(filename=storage)
                LOGGER.debug(f'截取当前页面，图片保存路径：{storage}')

            end_time = datetime.datetime.now()
            LOGGER.debug(f'用例（{func_name}）结束时间：{start_time}，耗时：{(end_time - start_time).total_seconds()}s')
        return wrapper
    return decorator
