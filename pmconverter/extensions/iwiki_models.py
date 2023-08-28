#!/usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@file: iwiki_models
@author: ghnjk
@create: 2023/8/27
"""
import datetime

from pmconverter.basic_model import Node, CommonSimpleMark, CommonSimpleNode
from pmconverter.model_factory import register_node_class, register_mark_class, toggle_camel_compat_mode

__ATTACHMENT_URL__ = ""


class TextColorMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "textColor"


class UnsupportedMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "unsupportedMark"


class TextHighlightMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "textHighlight"


class AlignmentMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "alignment"


class EmMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "em"


class AnnotationMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "annotation"


class IndentationMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "indentation"


class FontSizeMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "fontSize"


class Rule(CommonSimpleNode):

    def __init__(self):
        super().__init__()
        self.type = "rule"


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


class Panel(CommonSimpleNode):

    def __init__(self):
        super().__init__()
        self.type = "panel"


class Extension(CommonSimpleNode):

    def __init__(self):
        super().__init__()
        self.type = "extension"


class Expand(CommonSimpleNode):

    def __init__(self):
        super().__init__()
        self.type = "expand"

    def convert_to_markdown(self, **kwargs) -> str:
        title = self.get_attr("title", "")
        md = CommonSimpleNode.convert_to_markdown(self, **kwargs)
        return f"**{title}**\n{md}"


class Status(Node):

    def __init__(self):
        super().__init__()
        self.type = "status"

    def convert_to_markdown(self, **kwargs) -> str:
        text = self.get_attr("text", "")
        return f"**{text}**"


class Mention(Node):

    def __init__(self):
        super().__init__()
        self.type = "mention"

    def convert_to_markdown(self, **kwargs) -> str:
        text = self.get_attr("text", "")
        return f"**{text}**"


class Date(Node):

    def __init__(self):
        super().__init__()
        self.type = "date"

    def convert_to_markdown(self, **kwargs) -> str:
        timestamp = int(int(self.get_attr("timestamp", "")) / 1000)
        date_str = datetime.datetime.fromtimestamp(
            timestamp
        ).strftime('%Y-%m-%d %H:%M:%S')
        return f"**{date_str}**"


class TaskList(CommonSimpleNode):

    def __init__(self):
        super().__init__()
        self.type = "taskList"


class TaskItem(CommonSimpleNode):

    def __init__(self):
        super().__init__()
        self.type = "taskItem"


def load_iwiki_extensions(attachment_url: str = ""):
    global __ATTACHMENT_URL__
    __ATTACHMENT_URL__ = attachment_url
    toggle_camel_compat_mode()
    register_mark_class("textColor", TextColorMark)
    register_mark_class("annotation", AnnotationMark)
    register_mark_class("textHighlight", TextHighlightMark)
    register_mark_class("indentation", IndentationMark)
    register_mark_class("alignment", AlignmentMark)
    register_mark_class("em", EmMark)
    register_mark_class("fontSize", FontSizeMark)
    register_mark_class("unsupportedMark", UnsupportedMark)
    register_node_class("inlineExtension", InlineExtension)
    register_node_class("panel", Panel)
    register_node_class("status", Status)
    register_node_class("rule", Rule)
    register_node_class("extension", Extension)
    register_node_class("expand", Expand)
    register_node_class("date", Date)
    register_node_class("taskList", TaskList)
    register_node_class("taskItem", TaskItem)
    register_node_class("mention", Mention)
