# prosemirror-py-converter

[English Documents](README.md)

ProseMirror文档转markdown的python实现

## 核心功能

- 基于[ProseMirror基本模型](https://prosemirror.net/docs/ref/#model)，可支持自定义扩展的ProseMirror文档转换器
- 支持ProseMirror格式的Json转Markdown
- 支持的标准的ProseMirror基本格式和及其基础上的扩展
- 主要用于爬取和分析ProseMirror格式文档后的数据分析和展示用的。

## 快速上手

- 安装

```
pip3 install prosemirror-py-converter
```

- ProseMirror文档转Markdown

```
from pmconverter import prose2markdown

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
print(prose2markdown(doc))
```

- 输出markdown

```
### Example heading.
```

## 支持的标准ProseMirror格式

- [标准ProseMirror实现](pmconverter/prose_mirror_std_models.py)

### mark 列表

- link
- bold
- strong
- code
- italic
- strike
- subscript
- superscript
- underline

### node 列表

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

## 基于ProseMirror扩展的Mark和Node的转换支持

[iwiki doc converter](pmconverter/extensions/iwiki_models.py)

- 自定义Mark样例

```
from pmconverter.basic_model import CommonSimpleMark
from pmconverter.model_factory import register_mark_class


class CustomMark(CommonSimpleMark):

    def __init__(self):
        super().__init__()
        self.type = "custom_mark"
        self.md_pre_mark = "<u>"
        self.md_after_mark = "</u>"


register_mark_class("custom_mark", CustomMark)
```

- 自定义Node样例

```
from pmconverter.basic_model import Node
from pmconverter.model_factory import register_node_class


class CustomeImage(Node):

    def __init__(self):
        super().__init__()
        self.type = "custom_image"

    def convert_to_markdown(self, **kwargs) -> str:
        name = self.get_attr("name", "")
        url = self.get_attr("url", "")
        return f"![{name}]({url})"
        

register_node_class("custom_image", CustomeImage)
```