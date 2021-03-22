# -*- coding:utf-8 -*-
"""
浏览器驱动模块，提供driver各种操作方法
"""

import os
import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.loggers import LOGGER


class DriverBase(object):

    def __init__(self, driver='Chrome', enable_headless=False, enable_no_picture=False):
        """
        Browser driver初始化
        :param driver: 浏览器驱动
        :param enable_headless: 是否启动无界面模式，默认False
        :param enable_no_picture: 是否不加载图片，加快访问速度，默认False
        """
        # 浏览器选项配置
        chrome_options = webdriver.ChromeOptions()
        if enable_headless:
            chrome_options.add_argument('--headless')
        if enable_no_picture:
            chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

        # 选择浏览器驱动
        if driver == 'Firefox':
            self.driver = webdriver.Firefox(options=chrome_options)
        elif driver == 'Ie':
            self.driver = webdriver.Ie(options=chrome_options)
        else:
            self.driver = webdriver.Chrome(options=chrome_options)
        LOGGER.debug(f'加载浏览器驱动：{driver}')

        self.waiting = WebDriverWait(self.driver, 30)  # 设置显示等待30秒
        self.driver.implicitly_wait(30)  # 设置隐示等待30秒
        self.actions = webdriver.ActionChains(self.driver)  # 动作链初始化

    def find_element(self, locator, condition='presence', retries=1):
        """
        通过等待条件定位元素
        :param locator: 定义元组。例：(By.ID, '//*[@id="kw"]')
        :param condition: 等待条件
        :param retries: 重试次数，默认1
        :return: node or None
        """
        error_info = None
        for times in range(retries + 1):
            try:
                LOGGER.debug(f'定位元素：{locator}')
                if condition == 'visibility':  # 等待节点可见
                    node = self.waiting.until(EC.visibility_of_element_located(locator))
                else:  # 等待节点加载出来
                    node = self.waiting.until(EC.presence_of_element_located(locator))
                break
            except Exception as ex:
                error_info = f'定位 {locator} 失败，错误信息：{ex}'
                LOGGER.error(error_info)
                if times < retries:
                    LOGGER.warning(f'正在重试，当前重试次数：{times}，总数：{retries}')
                    time.sleep(1)
        else:
            raise Exception(error_info)
        return node

    def click_button(self, locator):
        """
        点击按钮
        :param locator:
        :return:
        """
        node = self.find_element(locator)
        node.click()
        time.sleep(1)

    def send_keys(self, locator, value, directly_enter=False):
        """
        输入信息到文本框
        :param locator: 定位元组
        :param value: 输入值
        :param directly_enter: 是否直接回车，默认False
        :return:
        """
        node = self.find_element(locator)
        node.clear()  # 清空文本
        node.send_keys(value)  # 输入值
        LOGGER.debug(f'输入值：{value}')

        if directly_enter:
            node.send_keys(Keys.ENTER)  # 回车
            LOGGER.debug('执行回车')
        time.sleep(1)

    @staticmethod
    def get_node_detail_info(node):
        """
        获取当前节点的详细信息
        :param node:
        :return:
        """
        info = {
            'class_name': node.get_attribute('class', ''),  # 获取节点的class属性值
            'id': node.id,  # 获取节点的id值
            'text': node.text,  # 获取节点的文本值
            'location': node.location,  # 获取节点在页面中的相对位置
            'tag_name': node.tag_name,  # 获取节点的标签名称
            'size': node.size,  # 获取节点的大小
        }
        return info

    def get_current_page_source(self):
        """获取当前页面的源代码"""
        return self.driver.page_source

    def get_current_url(self):
        """获取当前页面的URL"""
        return self.driver.current_url

    def back(self):
        """网页后退"""
        self.driver.back()
        LOGGER.debug('网页后退')

    def forward(self):
        """网页前进"""
        self.driver.forward()
        LOGGER.debug('网页前进')

    def refresh(self):
        """网页刷新"""
        self.driver.refresh()
        LOGGER.debug('网页刷新')

    def get_page_cookies(self, name=None):
        """
        获取当前页面的cookies
        :param name: 如果有值，获取指定cookie，为None的时候获取所有cookie
        :return:
        """
        if name:
            return self.driver.get_cookie(name='key')
        return self.driver.get_cookies()

    def add_cookies(self, cookies={}):
        """
        添加cookies到driver
        :param cookies: 字典类型
        :return:
        """
        self.driver.add_cookie(cookies)
        LOGGER.debug(f'添加cookies：{cookies}')

    def delete_cookies(self):
        """删除当前页面所有的cookies"""
        self.driver.delete_all_cookies()
        LOGGER.debug(f'删除所有cookies')

    def switch_to_windows(self, to_parent_windows=False):
        """
        切换到不同的windows窗口
        :param to_parent_windows: 是否回到主窗口，默认False
        :return:
        """
        total = self.driver.window_handles
        if to_parent_windows:
            self.driver.switch_to.window(total[0])
        else:
            current_windows = self.driver.current_window_handle
            for window in total:
                if window != current_windows:
                    self.driver.switch_to.window(window)
        LOGGER.debug(f'切换windows窗口')

    def switch_to_frame(self, index=0, to_parent_frame=False, to_default_frame=False):
        """
        切换到不同的frame框架
        :param index: expect by frame index value or id or name or element
        :param to_parent_frame: 是否切换到上一个frame，默认False
        :param to_default_frame: 是否切换到最上层的frame，默认False
        :return:
        """
        if to_parent_frame:
            self.driver.switch_to.parent_frame()
        elif to_default_frame:
            self.driver.switch_to.default_content()
        else:
            self.driver.switch_to.frame(index)
        LOGGER.debug(f'切换frame，to：{index}')

    def open_windows(self, url=''):
        """
        请求URL，打开windows窗口
        :param url:
        :return:
        """
        self.driver.get(url)
        LOGGER.debug(f'打开网址：{url}')
        time.sleep(1)

    def open_new_windows(self, url=''):
        """
        打开一个新的windows窗口
        :param url: URL
        :return:
        """
        js = "window.open({})".format(url)
        LOGGER.debug(f'打开新网址：{url}')
        self.driver.execute_script(js)
        time.sleep(1)

    def page_scrolling(self, go_to_bottom=False, rolling_distance=(0, 1000), wait_time=5):
        """
        页面滚动，如果没有滚动效果，添加延时（页面需要全部加载完毕才能滚动）
        :param bool go_to_bottom: 是否直接滚动到当前页面的最底部，默认False
        :param tuple rolling_distance: 滚动距离，默认是向下滚动1000像素
        :param int wait_time: 滚动前的页面等待时间，默认5秒
        :return:
        """
        time.sleep(wait_time)
        if go_to_bottom:
            js = "window.scrollTo(0, document.body.scrollHeight)"
        else:
            js = "window.scrollBy({}, {})".format(rolling_distance[0], rolling_distance[1])
        self.driver.execute_script(js)
        LOGGER.debug(f'页面滚动完毕')

    def screenshot(self, storage_path, picture_name):
        """
        截取当前网页并保存为图片
        :param storage_path: 图片存储的路径
        :param picture_name: 图片名称
        :return:
        """
        current_times = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        storage = os.path.join(storage_path, f'{current_times}_{picture_name}.jpg')

        self.driver.save_screenshot(storage)
        LOGGER.debug(f'截取当前页面，图片保存路径：{storage}')

    def action_chain(self, source, target):
        """
        执行鼠标拖曳

        Example：
            source = self.driver.find_element_by_xpath('//*[@id="result_logo"]/img[1]')
            target = self.driver.find_element_by_xpath('//*[@id="kw"]')
            self.action_chain(source=source, target=target)

        :param source: 拖曳前位置
        :param target: 拖曳后位置
        :return:
        """
        self.actions.drag_and_drop(source, target)
        self.actions.perform()
        LOGGER.debug(f'执行鼠标拖曳，拖曳前位置：{source}，拖曳后位置：{target}')
        time.sleep(1)

    def close_current_windows(self):
        """关闭当前页面"""
        if self.driver:
            self.driver.close()
        LOGGER.debug(f'关闭当前页面')

    def quit_browser(self):
        """关闭所有页面，退出浏览器"""
        if self.driver:
            self.driver.quit()
        LOGGER.debug('退出浏览器')
