from setuptools import setup

setup(
    name='HupuLive',
    version='1.1',
    author='chenjiandongx',
    author_email='chenjiandongx@qq.com',
    url = "https://github.com/chenjiandongx/HupuLive",
    description='Proudly presented by Hupu JRs',
    license="MIT",
    py_modules=['hupu'],
    requires=["bs4"],
    entry_points={
        'console_scripts': [
            'hupu=hupu:cli'
        ]
    }
)

