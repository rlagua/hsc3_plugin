from collections import OrderedDict
from itertools import cycle
from xdist.scheduler import LoadScopeScheduling
import logging

# 设置日志
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Hsc3Scheduler(LoadScopeScheduling):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _split_scope(self, nodeid: str) -> str:
        if 're' in nodeid:
            # check the index of ']' to avoid the case: parametrize mark value has '@'
            return 're'
        else:
            return nodeid

def pytest_xdist_make_scheduler(log, config):
    return Hsc3Scheduler(config, log)
