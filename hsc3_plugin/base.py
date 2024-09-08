import logging


import pytest


# 设置logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class BasePlugin:

    @pytest.hookimpl
    def pytest_sessionstart(self, session: pytest.Config):
        logger.debug("pytest_sessionstart")
        # session.config.hook.pytest_hsc3_sessionstart(session=session)
        session.config.hook.pytest_hsc3_comm(session=session)

    @pytest.hookimpl
    def pytest_sessionfinish(self, session: pytest.Config, exitstatus):
        logger.debug("pytest_sessionfinish")
        # session.config.hook.pytest_hsc3_sessionfinish(session)

    @pytest.hookimpl
    def pytest_addhooks(self, pluginmanager):
        logger.debug("pytest_addhooks")

    @pytest.hookimpl
    def pytest_configure(self, config):
        logger.debug("pytest_configure")

    @pytest.hookimpl
    def pytest_unconfigure(self, config):
        logger.debug("pytest_unconfigure")

    @pytest.hookimpl
    def pytest_collectstart(self, collector):
        logger.debug("pytest_collectstart")

    @pytest.hookimpl
    def pytest_collectreport(self, report):
        logger.debug("pytest_collectreport")

    @pytest.hookimpl
    def pytest_collection_modifyitems(self, session, config, items):
        logger.debug("pytest_collection_modifyitems called")

    @pytest.hookimpl
    def pytest_collection_finish(self, session):
        logger.debug("pytest_collection_finish called")

    @pytest.hookimpl
    def pytest_runtestloop(self, session):
        logger.debug("pytest_runtestloop")
        # return session.config.hook.pytest_hsc3_protocol(session=session)

    @pytest.hookimpl
    def pytest_runtest_protocol(self, item, nextitem):
        logger.debug("pytest_runtest_protocol")

    @pytest.hookimpl
    def pytest_runtest_logstart(self, nodeid, location):
        logger.debug("pytest_runtest_logstart")

    @pytest.hookimpl
    def pytest_runtest_logfinish(self, nodeid, location):
        logger.debug("pytest_runtest_logfinish")

    @pytest.hookimpl
    def pytest_runtest_setup(self, item):
        logger.debug("pytest_runtest_setup")

    @pytest.hookimpl
    def pytest_runtest_call(self, item):
        logger.debug("pytest_runtest_call")

    @pytest.hookimpl
    def pytest_runtest_teardown(self, item, nextitem):
        logger.debug("pytest_runtest_teardown")

    @pytest.hookimpl
    def pytest_runtest_makereport(self, item, call):
        logger.debug("pytest_runtest_makereport called")

    @pytest.hookimpl
    def pytest_runtest_logreport(self, report):
        logger.debug("pytest_runtest_logreport")

    @pytest.hookimpl
    def pytest_itemcollected(self, item):
        logger.debug("pytest_itemcollected")

    @pytest.hookimpl
    def pytest_report_to_serializable(self, config, report):
        logger.debug("pytest_report_to_serializable")

    @pytest.hookimpl
    def pytest_report_from_serializable(self, config, data):
        logger.debug("pytest_report_from_serializable")

    @pytest.hookimpl
    def pytest_terminal_summary(self, terminalreporter, exitstatus, config):
        logger.debug("pytest_terminal_summary")

    @pytest.hookimpl
    def pytest_assertrepr_compare(self, config, op, left, right):
        logger.debug("pytest_assertrepr_compare")

    @pytest.hookimpl
    def pytest_exception_interact(self, node, call, report):
        logger.debug("pytest_exception_interact")
