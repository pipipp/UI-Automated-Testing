# -*- coding:utf-8 -*-
import os
import allure
import pytest
import requests

from utils.tools import get_yaml_test_data
from utils.allures import add_common_report
from config.settings import MODULE_DIR

# 获取测试数据
cases, params = get_yaml_test_data(os.path.join(MODULE_DIR['test_data_dir'], 'test_proxy.yaml'))


@allure.feature('proxy接口功能')
class TestProxy(object):

    @pytest.fixture(scope='function')
    def preparation(self):
        """测试的准备与收尾"""
        print('在数据库中准备测试数据')
        test_data = '在数据库中准备测试数据'
        yield test_data
        print('清理测试数据')

    @allure.story('测试代理IP获取')
    @pytest.mark.parametrize('case,http,expected', params, ids=cases)
    def test_proxy(self, env, case, http, expected):
        # 添加报告信息
        add_common_report(case, http, expected)

        # 开始测试
        r = requests.request(http['method'],
                             url=env['host'] + http['path'],
                             headers=http['headers'],
                             params=http['params'])
        resp = r.json()

        assert resp['status'] == expected['response']['status']
        assert resp['message'] == expected['response']['message']
        assert bool(resp['data']) == expected['response']['data']
