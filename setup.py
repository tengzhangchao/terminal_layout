# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-

__author__ = 'gojuukaze'

from setuptools import setup, find_packages

setup(
    name="terminal_layout",
    version="1.0.0",
    description="The project help you to quickly build layouts in terminal (命令行ui布局工具)",
    long_description=open("README.rst").read(),
    license="GUN V3.0",

    url="https://github.com/gojuukaze/terminal_layout",
    author="gojuukaze",
    author_email="i@ikaze.uu.me",

    packages=find_packages(exclude=['demo', 'tests']),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    include_package_data=True,
    platforms="OSX, Linux",
    install_requires=['colorama==0.4.1',
                      'colored==1.3.93'],
    tests_require=['colorama==0.4.1',
                   'colored==1.3.93'],

    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Terminals',
    ],
)