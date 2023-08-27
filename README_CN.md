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
