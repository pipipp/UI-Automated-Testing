# -*- coding:utf-8 -*-
"""
项目环境配置
"""

import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 各模块目录
MODULE_DIR = {
    'config_dir': os.path.join(BASE_DIR, 'config'),  # 配置文件目录
    'test_data_dir': os.path.join(BASE_DIR, 'test_data'),  # 测试数据目录
    'test_scripts_dir': os.path.join(BASE_DIR, 'test_scripts'),  # 测试脚本目录
}
