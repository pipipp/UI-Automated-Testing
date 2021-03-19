# -*- coding:utf-8 -*-
"""
工具模块
"""

import os
import yaml
import pandas as pd


def get_yaml_test_data(filepath):
    """
    获取Yaml文件的测试数据
    :param filepath: 文件路径
    :return:
    """
    result = []
    with open(filepath) as f:
        data = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = data['tests']
        for each in test:
            result.append(tuple(each.values()))
    return result


def get_excel_test_data(filepath, sheet_name):
    """
    获取Excel表格的测试数据
    :param filepath: 文件路径
    :param sheet_name: 工作表名
    :return: 包含所有行的列表
    """
    data = pd.read_excel(filepath, sheet_name=sheet_name)  # 读取表格
    data.fillna('', inplace=True)  # 替换所有的缺失值为空字符""
    new_list = data.values.tolist()
    return new_list
