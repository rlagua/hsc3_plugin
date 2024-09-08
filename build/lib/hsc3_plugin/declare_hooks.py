import logging
import pytest


# 设置 logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


@pytest.hookspec()
def pytest_hsc3_protocol(item, config):
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

