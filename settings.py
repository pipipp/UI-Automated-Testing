# -*- coding:utf-8 -*-
"""
项目环境配置
"""

import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 各模块目录
MODULE_DIR = {
    'logs_dir': os.path.join(BASE_DIR, 'logs'),  # 日志模块目录
    'test_data_dir': os.path.join(BASE_DIR, 'test_data'),  # 测试数据目录
    'failure_screenshot': os.path.join(BASE_DIR, 'failure_screenshot'),  # 失败截图目录
}

# 日志文件配置
LOG_CONFIG = {
    'formatter': '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
    'console_output_level': 'DEBUG',
    'file_output_level': 'DEBUG',
    'log_file_name': os.path.join(MODULE_DIR['logs_dir'], f'UI-Test.log'),
    'backup_count': 5,
}
