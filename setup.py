from setuptools import setup

setup(
    name='payara',
    version='0.0.1',
    url="https://github.com/zeekay/payara",
    author='Zach Kelling',
    author_email='zeekayy@gmail.com',
    packages=['payara'],
    description='A tool for rapid web development',
    install_requires=['boto', 'bottle'],
    scripts=['bin/payara'],
)
