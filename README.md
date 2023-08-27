# prosemirror-py-converter

[中文文档](README_CN.md)

Python simple implementation of converting ProseMirror doc to markdown

## core features

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
