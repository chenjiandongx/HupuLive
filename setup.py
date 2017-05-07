from setuptools import setup

setup(
    name='hupu',
    version='1.0',
    author='chenjiandongx',
    author_email='chenjiandongx@qq.com',
    url = "https://github.com/chenjiandongx/HupuLive",
    description='Proudly presented by Hupu JRs',
    license="MIT",
    py_modules=['hupu'],
    entry_points={
        'console_scripts': [
            'hupu=hupu:cli'
        ]
    }
)

