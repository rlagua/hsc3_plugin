
import logging

# 设置logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class BasePlugin:

    def pytest_sessionstart(self, session):
        logger.debug("pytest_sessionstart")

    def pytest_sessionfinish(self, session, exitstatus):
        logger.debug("pytest_sessionfinish")

    def pytest_addhooks(self, pluginmanager):
        logger.debug("pytest_addhooks")

    def pytest_configure(self, config):
        logger.debug("pytest_configure")

    def pytest_unconfigure(self, config):
        logger.debug("pytest_unconfigure")

    def pytest_collectstart(self, collector):
        logger.debug("pytest_collectstart")

    def pytest_collectreport(self, report):
        logger.debug("pytest_collectreport")

    def pytest_collection_modifyitems(self, session, config, items):
        logger.debug("pytest_collection_modifyitems called")

    def pytest_collection_finish(self, session):
        logger.debug("pytest_collection_finish called")

    def pytest_runtestloop(self, session):
        logger.debug("pytest_runtestloop before")
        for item in session.items:
            session.config.hook.pytest_hsc3_protocol(item=item, config=session.config)
            session.config.hook.pytest_runtest_protocol(item=item, nextitem=None)

        logger.debug("pytest_runtestloop after")
        # return True

    def pytest_runtest_protocol(self, item, nextitem):
        logger.debug("pytest_runtest_protocol")

    def pytest_runtest_logstart(self, nodeid, location):
        logger.debug("pytest_runtest_logstart")

    def pytest_runtest_logfinish(self, nodeid, location):
        logger.debug("pytest_runtest_logfinish")

    def pytest_runtest_setup(self, item):
        logger.debug("pytest_runtest_setup")

    def pytest_runtest_call(self, item):
        logger.debug("pytest_runtest_call")

    def pytest_runtest_teardown(self, item, nextitem):
        logger.debug("pytest_runtest_teardown")

    def pytest_runtest_makereport(self, item, call):
        logger.debug("pytest_runtest_makereport called")

    def pytest_runtest_logreport(self, report):
        logger.debug("pytest_runtest_logreport")

    def pytest_itemcollected(self, item):
        logger.debug("pytest_itemcollected")

    def pytest_report_to_serializable(self, config, report):
        logger.debug("pytest_report_to_serializable")

    def pytest_report_from_serializable(self, config, data):
        logger.debug("pytest_report_from_serializable")

    def pytest_terminal_summary(self, terminalreporter, exitstatus, config):
        logger.debug("pytest_terminal_summary")

    def pytest_assertrepr_compare(self, config, op, left, right):
        logger.debug("pytest_assertrepr_compare")

    def pytest_exception_interact(self, node, call, report):
        logger.debug("pytest_exception_interact")
