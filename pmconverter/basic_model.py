#!/usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@file: basic_model
@author: ghnjk
@create: 2023/8/27
"""
from typing import Optional


class Mark(object):
    """
    A mark is a piece of information that can be attached to a node, such as it being emphasized, in code font, or a link. It has a type and optionally a set of attributes that provide further information (such as the target of the link).
    """

    def __init__(self):
        self.type: str = ""
        self.attrs: Optional[dict[str, any]] = None

    def get_attr(self, key: str, default_value: any = None):
        if self.attrs is None:
            return default_value
        return self.attrs.get(key, default_value)

    def deserialize(self, d: dict):
        """
        deserialize from dict
        :param d: dict contain the information of mark
        """
        self.type = d["type"]
        self.attrs = d.get("attrs")

    def serialize(self) -> dict:
        """
        serialize mark to dict for persist.
        :return: the information describe current mark
        """
        return {
            "type": self.type,
            "attrs": self.attrs
        }

    def add_markdown_marks(self, md_body: str, **kwargs) -> str:
        """
        add markdown marks to md_body
        :param md_body: markdown body str
        :param kwargs: convert options
        :return: marked markdown str
        """
        raise NotImplementedError("add_markdown_marks not implemented.")


class Node(object):
    """
    This class represents a node in the tree that makes up a ProseMirror document. So a document is an instance of Node, with children that are also instances of Node.
    """

    def __init__(self):
        self.type: str = "node"
        self.content: Optional[list[Node]] = None
        self.text: Optional[str] = None
        self.attrs: Optional[dict[str, any]] = None
        self.marks: Optional[list[Mark]] = None

    def convert_to_markdown(self, **kwargs) -> str:
        """
        convert current node to markdown
        :param kwargs: convert options
        :return: markdown str
        """
        raise NotImplementedError("convert_to_markdown not implemented.")

    def get_attr(self, key: str, default_value: any = None):
        if self.attrs is None:
            return default_value
        return self.attrs.get(key, default_value)

    def deserialize(self, d: dict):
        """
        deserialize from dict
        :param d: dict contain the information of node
        """
        from pmconverter.model_factory import build_node, build_mark
        self.type = d["type"]
        self.text = d.get("text")
        self.attrs = d.get("attrs")
        # use model_factory.build_mark to deserialize marks
        mark_dicts = d.get("marks")
        if mark_dicts is None:
            self.marks = None
        else:
            self.marks = []
            for md in mark_dicts:
                self.marks.append(build_mark(md))
        # use model_factory.build_node to deserialize children node
        content_dicts = d.get("content")
        if content_dicts is None:
            self.content = None
        else:
            self.content = []
            for cd in content_dicts:
                self.content.append(build_node(cd))

    def serialize(self) -> dict:
        """
        serialize current node to dict for persist.
        :return: the information describe current node
        """
        return {
            "type": self.type,
            "text": self.text,
            "content": None if self.content is None else [
                c.serialize() for c in self.content],
            "attrs": self.attrs,
            "marks": None if self.marks is None else [
                m.serialize() for m in self.marks]}


class CommonSimpleMark(Mark):

    def __init__(self):
        super().__init__()
        self.md_pre_mark: str = ""
        self.md_after_mark: str = ""

    def add_markdown_marks(self, md_body: str, **kwargs) -> str:
        return f"{self.md_pre_mark}{md_body}{self.md_after_mark}"


class CommonSimpleNode(Node):

    def convert_to_markdown(self, **kwargs) -> str:
        md = ""
        if self.text is not None:
            md += self.text
        if self.content is not None:
            if len(md) > 0:
                md += "\n"
            for idx, c in enumerate(self.content):
                md += c.convert_to_markdown(**kwargs)
                if idx < len(self.content) - 1:
                    md += "\n"
        if self.marks is not None:
            for m in self.marks:
                md = m.add_markdown_marks(md, **kwargs)
        return md
