#!/usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@file: setup
@author: ghnjk
@create: 2023/8/26
"""
from setuptools import setup

setup(
    name='prosemirror-py-converter',
    version='0.1',
    author='ghnjk',
    author_email='ghnjk@foxmail.com',
    url='https://github.com/ghnjk/prosemirror-py-converter',
    description=u'Python simple implementation of converting ProseMirror doc to markdown',
    long_description="python simple implementation of prosemirror doc json to markdown format docs.",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    packages=['pmconverter'],
    install_requires=[],
    license='MIT',
    keywords='prosemirror markdown pmconverter html python-converter'
)
