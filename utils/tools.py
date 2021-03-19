# -*- coding:utf-8 -*-
"""
工具模块
"""

import yaml


def get_yaml_test_data(filepath):
    """
    获取yaml文件的测试数据
    :param filepath: 文件路径
    :return:
    result = ([case_1, case_2 ...], [(case_1, http, expected), (case_2, http, expected) ...])
    """
    case = []  # 存储测试用例名称
    http = []  # 存储请求对象
    expected = []  # 存储预期结果
    with open(filepath) as f:
        data = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = data['tests']
        for each in test:
            case.append(each.get('case', ''))
            http.append(each.get('http', {}))
            expected.append(each.get('expected', {}))
    params = list(zip(case, http, expected))  # 将每条用例解包在一起
    return case, params
