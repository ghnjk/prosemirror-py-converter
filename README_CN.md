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
