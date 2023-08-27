#!/usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@file: iwiki_models
@author: ghnjk
@create: 2023/8/27
"""
from pmconverter.basic_model import Node, CommonSimpleMark
from pmconverter.model_factory import register_node_class, register_mark_class, toggle_camel_compat_mode

__ATTACHMENT_URL__ = ""


class TextColorMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "textColor"


class TextHighlightMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "textHighlight"


class AlignmentMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "alignment"


class FontSizeMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "fontSize"


class InlineExtension(Node):

    def __init__(self):
        super().__init__()
        self.type = "inlineExtension"

    def convert_to_markdown(self, **kwargs) -> str:
        extension_type = self.get_attr("extensionType")
        parameters = self.get_attr("parameters", {})
        if extension_type == "com.tencent.iwiki.editor.image":
            name = parameters.get("name", "")
            att_id = parameters.get("id", -1)
            url = __ATTACHMENT_URL__ + str(att_id)
            return f"![{name}]({url})"
        else:
            return ""


def load_iwiki_extensions(attachment_url: str = ""):
    global __ATTACHMENT_URL__
    __ATTACHMENT_URL__ = attachment_url
    toggle_camel_compat_mode()
    register_mark_class("textColor", TextColorMark)
    register_mark_class("textHighlight", TextHighlightMark)
    register_mark_class("alignment", AlignmentMark)
    register_mark_class("fontSize", FontSizeMark)
    register_node_class("inlineExtension", InlineExtension)
