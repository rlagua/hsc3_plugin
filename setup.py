from setuptools import setup

setup(
    name="hsc3_plugin",  # 插件名称
    version="1.0.4",
    description="A custom pytest plugin with hsc3 option",
    author="Your Name",
    author_email="your_email@example.com",
    packages=["hsc3_plugin"],  # 插件代码所在的包名
    entry_points={
        "pytest11": [
            "hsc3_plugin = hsc3_plugin.plugin",  # 插件入口
        ],
    },
    install_requires=[
        "pytest>=3.0.0",  # 插件的依赖
    ],
    classifiers=[
        "Framework :: Pytest",
        "Programming Language :: Python :: 3",
    ],
)
