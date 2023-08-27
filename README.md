# prosemirror-py-converter

[中文指引](README_CN.md)

Python simple implementation of converting ProseMirror doc to markdown

## Core features

- Based on [ProseMirror basic model](https://prosemirror.net/docs/ref/#model)
- Support custom extension
- ProseMirror document converter: Json to Markdown in ProseMirror format
- Mainly used for data analysis and display after spider ProseMirror documents.

## Quick start

- Install prosemirror-py-converter

```
pip3 install prosemirror-py-converter
```

- Convert ProseMirror document to Markdown

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

- output markdown

```
### Example heading.
```

## Standard ProseMirror implementation

- [Standard ProseMirror implementation](pmconverter/prose_mirror_std_models.py)

### mark type list

- link
- bold
- strong
- code
- italic
- strike
- subscript
- superscript
- underline

### node type list

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

## Custom ProseMirror extension examples

[iwiki doc converter](pmconverter/extensions/iwiki_models.py)

- custom mark converter example

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

- custom node converter example

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