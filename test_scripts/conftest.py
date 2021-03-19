# -*- coding:utf-8 -*-
"""
Hook fixture 通用模块

conftest.py是一个plugin文件（固定名称）：
    里面可以实现Pytest提供的Hook函数或者自定义的fixture函数
    这些函数只在conftest.py所在目录及其子目录中生效

request.config.rootdir属性：
    这个属性表示的是pytest.ini这个配置文件所在的目录
"""
import os
import yaml
import pytest


def pytest_addoption(parser):
    """
    添加pytest命令行选项
    :param parser:
    :return:
    """
    parser.addoption("--env",
                     action="store",
                     dest="environment",  # 参数名称
                     default="test",  # 默认值
                     help="environment: test or prod")


@pytest.fixture(scope='session')  # 作用于整个测试
def env(request):
    """获取config目录里面的环境配置文件"""
    config_path = os.path.join(request.config.rootdir,
                               'config',
                               request.config.getoption('environment'),
                               'config.yaml')
    with open(config_path) as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return env_config
