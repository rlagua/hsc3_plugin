import time
import pytest


import logging

# 设置logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('log.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def test_recase1():
    time.sleep(1)
    pass

def test_recase2():
    pass


class TestRRR:
    def setup_class(self):
        logger.info('test RRR 的类级别setup')

    def teardown_method(self):
        logger.info('teardown test RRR d的 方法级别teardown')

    def test_rerun(self):
        logger.info('test rerun')

    def test_rewrite(self):
        assert False

    def test_areaq(self):
        logger.info(' test q')


if __name__ == '__main__':
    pytest.main(['-vs', '-n 2','--dist=load', __file__, '--hsc3=control'])