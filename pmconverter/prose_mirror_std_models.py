#!/usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@file: common_models
@author: ghnjk
@create: 2023/8/27
"""
from pmconverter.basic_model import Node, CommonSimpleNode, CommonSimpleMark
from pmconverter.model_factory import register_mark_class, register_node_class

"""
    standard prosemirror marks.
    mark list:
    - link
    - bold
    - strong
    - code
    - italic
    - strike
    - subscript
    - superscript
    - underline
"""


class LinkMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "link"

    def add_markdown_marks(self, md_body: str, **kwargs) -> str:
        href = self.get_attr("href", "")
        return f"[{md_body}]({href})"


register_mark_class("link", LinkMark)


class BoldMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "bold"
        self.md_pre_mark = "**"
        self.md_after_mark = "**"


register_mark_class("bold", BoldMark)


class StrongMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "strong"
        self.md_pre_mark = "**"
        self.md_after_mark = "**"


register_mark_class("strong", StrongMark)


class CodeMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "code"
        self.md_pre_mark = "```"
        self.md_after_mark = "```"


register_mark_class("code", CodeMark)


class ItalicMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "italic"
        self.md_pre_mark = "*"
        self.md_after_mark = "*"


register_mark_class("italic", ItalicMark)


class StrikeMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "strike"
        self.md_pre_mark = "~~"
        self.md_after_mark = "~~"


register_mark_class("strike", StrikeMark)


class SuperScriptMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "superscript"
        self.md_pre_mark = "> "
        self.md_after_mark = ""


register_mark_class("superscript", SuperScriptMark)


class SubscriptMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "subscript"
        self.md_pre_mark = "> "
        self.md_after_mark = ""


register_mark_class("subscript", SubscriptMark)


class UnderlineMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "underline"
        self.md_pre_mark = "<u>"
        self.md_after_mark = "</u>"


register_mark_class("underline", UnderlineMark)

"""
    standard prosemirror node.
    mark list:
    - doc
    - heading
    - paragraph
    - image
    - bullet_list
    - ordered_list
    - table
    - blockquote
    - code_block
    - hard_break
    - horizontal_rule
"""


class Doc(CommonSimpleNode):

    def __init__(self):
        super().__init__()
        self.type = "doc"


register_node_class("doc", Doc)


class Heading(CommonSimpleNode):

    def __init__(self):
        super().__init__()
        self.type = "heading"

    def convert_to_markdown(self, **kwargs) -> str:
        md = CommonSimpleNode.convert_to_markdown(self, **kwargs)
        level = int(self.get_attr("level", 1))
        if level <= 0:
            level = 1
        head_md = "#" * level
        return f"{head_md} {md}"


register_node_class("heading", Heading)


class Paragraph(CommonSimpleNode):

    def __init__(self):
        super().__init__()
        self.type = "paragraph"

    def convert_to_markdown(self, **kwargs) -> str:
        md = CommonSimpleNode.convert_to_markdown(self, **kwargs)
        return md + "\n"


register_node_class("paragraph", Paragraph)


class Text(CommonSimpleNode):

    def __init__(self):
        super().__init__()
        self.type = "text"


register_node_class("text", Text)


class BlockQuote(CommonSimpleNode):

    def __init__(self):
        super().__init__()
        self.type = "blockquote"

    def convert_to_markdown(self, **kwargs) -> str:
        md = CommonSimpleNode.convert_to_markdown(self, **kwargs)
        block_quoted_md = ""
        for line in md.split("\n"):
            block_quoted_md += "> " + line + "\n"
        return block_quoted_md


register_node_class("blockquote", BlockQuote)


class BulletList(Node):

    def __init__(self):
        super().__init__()
        self.type = "bullet_list"

    def convert_to_markdown(self, **kwargs) -> str:
        md = ""
        if self.content is not None:
            if len(md) > 0:
                md += "\n"
            for index, c in enumerate(self.content):
                md += f"{index + 1}. "
                md += c.convert_to_markdown(**kwargs)
                md += "\n"
        if self.marks is not None:
            for m in self.marks:
                md = m.add_markdown_marks(md, **kwargs)
        return md


register_node_class("bullet_list", BulletList)


class OrderedList(Node):

    def __init__(self):
        super().__init__()
        self.type = "ordered_list"

    def convert_to_markdown(self, **kwargs) -> str:
        md = ""
        if self.content is not None:
            if len(md) > 0:
                md += "\n"
            for c in self.content:
                md += f"- "
                md += c.convert_to_markdown(**kwargs)
                md += "\n"
        if self.marks is not None:
            for m in self.marks:
                md = m.add_markdown_marks(md, **kwargs)
        return md


register_node_class("ordered_list", OrderedList)


class ListItem(CommonSimpleNode):

    def __init__(self):
        super().__init__()
        self.type = "list_item"


register_node_class("list_item", ListItem)


class CodeBlock(CommonSimpleNode):

    def __init__(self):
        super().__init__()
        self.type = "code_block"

    def convert_to_markdown(self, **kwargs) -> str:
        md = CommonSimpleNode.convert_to_markdown(self, **kwargs)
        return f"```\n{md}\n```\n"


register_node_class("code_block", CodeBlock)


class HardBreak(Node):

    def __init__(self):
        super().__init__()
        self.type = "hard_break"

    def convert_to_markdown(self, **kwargs) -> str:
        return "\\"


register_node_class("hard_break", HardBreak)


class HorizontalRule(Node):

    def __init__(self):
        super().__init__()
        self.type = "horizontal_rule"

    def convert_to_markdown(self, **kwargs) -> str:
        return "---"


register_node_class("horizontal_rule", HorizontalRule)


class Image(Node):

    def __init__(self):
        super().__init__()
        self.type = "image"

    def convert_to_markdown(self, **kwargs) -> str:
        alt = self.get_attr("alt", "")
        src = self.get_attr("src", "")
        title = self.get_attr("title", "")
        return f"![{alt}]({src} \"{title}\")"


register_node_class("image", Image)


class Table(Node):

    def __init__(self):
        super().__init__()
        self.type = "table"

    def convert_to_markdown(self, **kwargs) -> str:
        if self.content is None or len(self.content) < 1:
            return ""
        th = self.content[0]
        if th.content is None or len(th.content) < 1:
            return ""
        table_header_md = th.convert_to_markdown(**kwargs)
        table_sep = "|"
        for i in range(len(th.content)):
            table_sep += " -- |"
        table_body_md = ""
        for i in range(1, len(self.content)):
            table_body_md += self.content[i].convert_to_markdown(**kwargs)
            table_body_md += "\n"
        return f"{table_header_md}\n{table_sep}\n{table_body_md}"


register_node_class("table", Table)


class TableRow(Node):

    def __init__(self):
        super().__init__()
        self.type = "table_row"

    def convert_to_markdown(self, **kwargs) -> str:
        md = "| "
        if self.content is not None:
            for idx, c in enumerate(self.content):
                if idx > 0:
                    md += " | "
                md += c.convert_to_markdown(**kwargs).strip()
        md += " |"
        if self.marks is not None:
            for m in self.marks:
                md = m.add_markdown_marks(md, **kwargs)
        return md


register_node_class("table_row", TableRow)


class TableHeader(CommonSimpleNode):

    def __init__(self):
        super().__init__()
        self.type = "table_header"


register_node_class("table_header", TableHeader)


class TableCell(CommonSimpleNode):

    def __init__(self):
        super().__init__()
        self.type = "table_cell"


register_node_class("table_cell", TableCell)
