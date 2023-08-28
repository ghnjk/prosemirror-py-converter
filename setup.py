#!/usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@file: setup
@author: ghnjk
@create: 2023/8/26
"""
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    long_description = long_description.replace(
        "[中文指引](README_CN.md)",
        "[中文指引](https://github.com/ghnjk/prosemirror-py-converter/blob/main/README_CN.md)"
    )
    long_description = long_description.replace(
        "(pmconverter/prose_mirror_std_models.py)",
        "(https://github.com/ghnjk/prosemirror-py-converter/blob/main/pmconverter/prose_mirror_std_models.py)"
    )
    long_description = long_description.replace(
        "(pmconverter/extensions/iwiki_models.py)",
        "(https://github.com/ghnjk/prosemirror-py-converter/blob/main/pmconverter/extensions/iwiki_models.py)"
    )

setup(
    name='prosemirror-py-converter',
    version='0.2',
    author='ghnjk',
    author_email='ghnjk@foxmail.com',
    url='https://github.com/ghnjk/prosemirror-py-converter',
    description=u'Python simple implementation of converting ProseMirror doc to markdown',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    packages=['pmconverter'],
    install_requires=[],
    license='MIT',
    keywords='prosemirror markdown pmconverter html python-converter'
)
