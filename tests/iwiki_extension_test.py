#!/usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@file: iwiki_extension_test
@author: ghnjk
@create: 2023/8/27
"""
import json
import os
import typing

import pytest

from pmconverter import prose2markdown


def load_test_data(file_dir: str, case_name: str) -> typing.Tuple[dict, str]:
    file_path = os.path.join(file_dir, f"{case_name}.json")
    if not os.path.isfile(file_path):
        raise Exception(f"test data file {file_path} not exist.")
    with open(file_path, "r") as fp:
        d = json.load(fp)
        return d["json"], d["markdown"]


def setup_module():
    from pmconverter.extensions.iwiki_models import load_iwiki_extensions
    load_iwiki_extensions("http://example.io/attachment?id=")


@pytest.mark.parametrize("file_dir", ["test_data/iwiki"])
@pytest.mark.parametrize(" case_name", [
    "normal_doc_1",
    "iwiki_doc_1",
    "iwiki_doc_2",
    "iwiki_doc_3",
])
def test_iwiki_converter(file_dir: str, case_name: str):
    doc, md = load_test_data(file_dir, case_name)
    assert prose2markdown(doc) == md
