import logging
import time
import socket

from threading import Thread

import pytest


# 设置 logger
logger = logging.getLogger(__name__)


# 实现自定义钩子
@pytest.hookimpl
def pytest_hsc3_protocol(session):
    value = session.config.getoption('--hsc3')
    if value == 'control':
        for ind in range(len(session.items)-1):
            item = session.items[ind]
            nextitem = session.items[ind + 1]
            logger.warning(f'警告，自定义执行进行中{item.nodeid}')
            session.config.hook.pytest_runtest_protocol(item=item, nextitem=nextitem)
            if 'rerun' in item.name:
                logger.info(f'重复执行 {item.nodeid}')
                session.config.hook.pytest_runtest_protocol(item=item, nextitem=nextitem)
        session.config.hook.pytest_runtest_protocol(item=session.items[-1], nextitem=None)
        
        return True

@pytest.hookimpl
def pytest_hsc3_comm(session):
    host = '127.0.0.1'
    port = 4455
    reconnect_delay = 3  # 重连延迟时间（秒）

    def create_socket():
        """创建一个新的 socket 连接"""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return s

    def worker():
        client = None
        session.config.hsc3_comm = client
        while True:
            if client is None:
                client = create_socket()

            try:
                # 尝试连接服务器
                logger.info(f"尝试连接到服务器 {host}:{port}...")
                client.connect((host, port))  # 只在未连接时调用
                logger.debug(f"已连接到服务器 {host}:{port}")

                while True:
                    try:
                        # 接收来自服务器的消息
                        response = client.recv(1024)
                        if response:
                            logger.info(f"接收到服务器消息: {response.decode('utf-8')}")
                            session.config.hook.pytest_hsc3_handler_message(msg=response.decode('utf-8'), session=session)
                        else:
                            raise ConnectionError("连接已断开")
                    except (ConnectionError, socket.error) as e:
                        logger.warning(f"接收消息时出错: {e}")
                        break  # 连接断开，跳出内层循环，重新连接
            except (ConnectionRefusedError, socket.error) as e:
                logger.warning(f"无法连接到服务器: {e}")
                client.close()
                client = None  # 重置客户端以进行重新连接

            logger.info(f"将在 {reconnect_delay} 秒后重试连接...")
            time.sleep(reconnect_delay)
    t = Thread(target=worker)
    t.daemon = True
    t.start()


@pytest.hookimpl
def pytest_hsc3_handler_message(msg, session):
    """comm"""
    if msg == 'skip':
        logger.warning('You are Skip current TestCase')
    if msg == 'get_items':
        for item in session.items:
            logger.info(item.nodeid)