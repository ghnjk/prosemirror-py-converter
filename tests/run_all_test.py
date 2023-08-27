#!/usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@file: run_all_test
@author: ghnjk
@create: 2023/8/28
"""
import os
import sys

import pytest


def run_all_test():
    pkg_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, pkg_path)
    test_dir = os.path.dirname(os.path.abspath(__file__))
    sys.exit(pytest.main(["-x", test_dir]))


if __name__ == '__main__':
    run_all_test()
