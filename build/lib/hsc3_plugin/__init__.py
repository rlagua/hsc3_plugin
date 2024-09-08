from hsc3_plugin.base import BasePlugin
from hsc3_plugin import realise_hooks
from hsc3_plugin import declare_hooks
from hsc3_plugin import addopts



def pytest_configure(config):
    config.pluginmanager.register(BasePlugin(), name="base_plugin")
    config.pluginmanager.register(addopts, name="addopts")
    config.pluginmanager.register(realise_hooks, name="newhooks")

# pytest 插件需要的钩子，用于注册自定义钩子
def pytest_addhooks(pluginmanager):
    # 没有hookspec和hookimpl装饰器，必须声明-添加hook再什么
    # hookspec声明的钩子，就算没有实现，也能调用
    pluginmanager.add_hookspecs(declare_hooks)

