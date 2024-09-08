import pytest
from hsc3_plugin.base import BasePlugin
from hsc3_plugin import realise_hooks
from hsc3_plugin import declare_hooks
from hsc3_plugin import schedule


def pytest_configure(config):
    config.pluginmanager.register(BasePlugin(), name="base_plugin")
    config.pluginmanager.register(realise_hooks, name="newhooks")
    config.pluginmanager.register(schedule, name="seched")

# pytest 插件需要的钩子，用于注册自定义钩子
def pytest_addhooks(pluginmanager):
    # 没有hookspec和hookimpl装饰器，必须声明-添加hook再什么
    # hookspec声明的钩子，就算没有实现，也能调用
    pluginmanager.add_hookspecs(declare_hooks)


@pytest.hookimpl
def pytest_addoption(parser: pytest.Parser) -> None:
    """必须在插件顶层注册，不然没法及时识别"""
    group = parser.getgroup("hsc3", "hsc3 robot control")
    group.addoption(
        "--hsc3",
        metavar="distmode",
        action="store",
        choices=[
            "control",
            "no",],
        default='no')