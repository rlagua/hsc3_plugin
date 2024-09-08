import time
import socket
import logging
from threading import Thread


import pytest


# 设置 logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@pytest.hookspec()
def pytest_hsc3_protocol(session):
    """
    Hookspec: 用于定义 pytest_hsc3_protocol 的接口。
    """
    pass


@pytest.hookspec()
def pytest_hsc3_colletion(item=None, config=None):
    """
    Hookspec: 用于定义 pytest_hsc3_protocol 的接口。
    """
    pass

@pytest.hookspec()
def pytest_hsc3_config(item=None, config=None):
    """
    Hookspec: 用于定义 pytest_hsc3_protocol 的接口。
    """
    pass

@pytest.hookspec()
def pytest_hsc3_sessionstart(session):
    """
    在 session 开始时创建一个 Twisted 的 socket 客户端。
    """
    pass

@pytest.hookspec()
def pytest_hsc3_sessionfinish(session):
    """在 session 结束时，停止 Twisted 事件循环"""
    pass

@pytest.hookspec()
def pytest_hsc3_comm(session):
    """comm"""
    pass

@pytest.hookspec()
def pytest_hsc3_handler_message(msg, session):
    """comm"""
    pass