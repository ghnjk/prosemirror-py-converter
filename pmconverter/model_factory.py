#!/usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@file: model_factory
@author: ghnjk
@create: 2023/8/27
"""
from pmconverter.basic_model import Node, Mark

__MARK_CLASS_MAP__ = {}
__CAMEL_COMPAT_MODE__ = False


def generate_camel_compat_keys(key: str) -> list[str]:
    all_keys = set()
    all_keys.add(key)
    fields = key.split("_")
    if len(fields) > 1:
        camel_key = fields[0]
        for i in range(1, len(fields)):
            camel_key += fields[i][0].upper() + fields[i][1:]
        all_keys.add(camel_key)
    fields = []
    cur = ""
    for c in key:
        if c.isupper():
            if len(cur) > 0:
                fields.append(cur)
                cur = ""
        cur += c.lower()
    if len(cur) > 0:
        fields.append(cur)
    all_keys.add("_".join(fields))
    return list(all_keys)


def register_mark_class(mark_type: str, mark_class: type):
    if __CAMEL_COMPAT_MODE__:
        for k in generate_camel_compat_keys(mark_type):
            __MARK_CLASS_MAP__[k] = mark_class
    else:
        __MARK_CLASS_MAP__[mark_type] = mark_class


def build_mark(mark_dict: dict) -> Mark:
    mark_type = mark_dict.get("type")
    if mark_type is None:
        raise Exception("invalid mark dict. type is required.")
    cls = __MARK_CLASS_MAP__.get(mark_type)
    if cls is None:
        raise Exception(f"not support mark type {mark_type}")
    m: Mark = cls()
    m.deserialize(mark_dict)
    return m


__NODE_CLASS_MAP__ = {}


def register_node_class(node_type: str, node_class: type):
    if __CAMEL_COMPAT_MODE__:
        for k in generate_camel_compat_keys(node_type):
            __NODE_CLASS_MAP__[k] = node_class
    else:
        __NODE_CLASS_MAP__[node_type] = node_class


def build_node(node_dict: dict) -> Node:
    node_type = node_dict.get("type")
    if node_type is None:
        raise Exception("invalid node dict. type is required.")
    cls = __NODE_CLASS_MAP__.get(node_type)
    if cls is None:
        raise Exception(f"not support node type {node_type}")
    n: Node = cls()
    n.deserialize(node_dict)
    return n


def toggle_camel_compat_mode():
    global __CAMEL_COMPAT_MODE__
    __CAMEL_COMPAT_MODE__ = True
    for key in list(__MARK_CLASS_MAP__.keys()):
        cls = __MARK_CLASS_MAP__[key]
        for k in generate_camel_compat_keys(key):
            __MARK_CLASS_MAP__[k] = cls
    for key in list(__NODE_CLASS_MAP__.keys()):
        cls = __NODE_CLASS_MAP__[key]
        for k in generate_camel_compat_keys(key):
            __NODE_CLASS_MAP__[k] = cls
