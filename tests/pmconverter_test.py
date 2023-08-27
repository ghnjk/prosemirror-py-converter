#!/usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@file: pmconverter_test
@author: ghnjk
@create: 2023/8/27
"""
import json
import os
import typing

import pytest

from pmconverter import prose2markdown


def test_camel_mode():
    from pmconverter.model_factory import toggle_camel_compat_mode, __MARK_CLASS_MAP__, __NODE_CLASS_MAP__
    toggle_camel_compat_mode()
    print("marks:")
    print("\n".join(__MARK_CLASS_MAP__.keys()))
    print("nodes:")
    print("\n".join(__NODE_CLASS_MAP__.keys()))


def test_basic_pmconverter():
    doc = {
        "type": "doc",
        "content": [
            {
                "type": "heading",
                "attrs": {
                    "level": 3
                },
                "content": [
                    {
                        "type": "text",
                        "text": "Example heading."
                    }
                ]
            }
        ]
    }
    assert "### Example heading." == prose2markdown(doc)


def load_test_data(file_dir: str, case_name: str) -> typing.Tuple[dict, str]:
    file_path = os.path.join(file_dir, f"{case_name}.json")
    if not os.path.isfile(file_path):
        raise Exception(f"test data file {file_path} not exist.")
    with open(file_path, "r") as fp:
        d = json.load(fp)
        return d["json"], d["markdown"]


@pytest.mark.parametrize("file_dir", ["test_data/marks"])
@pytest.mark.parametrize(" case_name", [
    "bold_mark_test",
    "code_mark_test",
    "italic_mark_test",
    "link_mark_test",
    "strike_mark_test",
    "subscript_mark_test",
    "underline_mark_test"
])
def test_mark_converter(file_dir: str, case_name: str):
    doc, md = load_test_data(file_dir, case_name)
    assert prose2markdown(doc) == md


@pytest.mark.parametrize("file_dir", ["test_data/nodes"])
@pytest.mark.parametrize(" case_name", [
    "block_quote_test",
    "bullet_list_test",
    "code_block_test",
    "hard_break_test",
    "heading_test",
    "horizontal_rule_test",
    "image_test",
    "ordered_list_test",
    "table_test"
])
def test_node_converter(file_dir: str, case_name: str):
    doc, md = load_test_data(file_dir, case_name)
    assert prose2markdown(doc) == md
