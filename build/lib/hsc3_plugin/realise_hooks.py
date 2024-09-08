import logging

import pytest


# 设置 logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


# 实现自定义钩子
@pytest.hookimpl
def pytest_hsc3_protocol(item, config):
    """
    自定义钩子的实现。
    """
    logger.info(f"自定义钩子：pytest_hsc3_protocol called with item: {item} {config}")
    if config:
        value = config.getoption('--hsc3')
        logger.info(f'hsc3 args {value}')