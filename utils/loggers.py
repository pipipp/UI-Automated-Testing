# -*- coding:utf-8 -*-
"""
日志模块
"""

import logging

from logging.handlers import TimedRotatingFileHandler
from settings import LOG_CONFIG


class Logger(object):

    def __init__(self, log_file_name, console_output_level='DEBUG', file_output_level='DEBUG',
                 backup_count=5, formatter='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        """
        日志文件初始化配置
        :param log_file_name: 日志文件的名称
        :param console_output_level: 控制台消息打印等级
        :param file_output_level: 日志文件消息打印等级
        :param backup_count: 最多存放日志的数量
        :param formatter: 日志消息格式
        """
        self.logger = logging.getLogger(__name__)
        logging.root.setLevel(logging.NOTSET)

        self.log_file_name = log_file_name
        self.backup_count = backup_count
        self.console_output_level = console_output_level
        self.file_output_level = file_output_level
        self.formatter = logging.Formatter(formatter)

    def get_logger(self):
        """在self.logger中添加日志句柄并返回，如果self.logger已有句柄，则直接返回"""
        if not self.logger.handlers:  # 避免重复日志

            # 创建一个handler，用于输出到控制台
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 创建一个handler，用于写入日志文件（设置每天创建新的日志文件，最多保留backup_count份）
            file_handler = TimedRotatingFileHandler(filename=self.log_file_name,
                                                    when='D', interval=1, backupCount=self.backup_count,
                                                    delay=True, encoding='utf-8')
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger


LOGGER = Logger(LOG_CONFIG['log_file_name'], LOG_CONFIG['console_output_level'], LOG_CONFIG['file_output_level'],
                LOG_CONFIG['backup_count'], LOG_CONFIG['formatter']).get_logger()
