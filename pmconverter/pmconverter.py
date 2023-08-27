#!/usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@file: pmconverter
@author: ghnjk
@create: 2023/8/27
"""
from pmconverter.model_factory import build_node


def prose2markdown(doc: dict, **kwargs) -> str:
    node = build_node(doc)
    return node.convert_to_markdown(**kwargs)
