import unittest
from app.leafnode import LeafNode
from app.parentnode import ParentNode
from app.markdown_to_htmlnode import (
    markdown_to_htmlnode,
    text_to_children
)


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_heading(self):
        markdown = "# Heading"
        result = markdown_to_htmlnode(markdown)
        expected = ParentNode('div', [ParentNode('h1', text_to_children("Heading"))])
        self.assertEqual(result, expected)

    def test_code_block(self):
        markdown = "```code```"
        result = markdown_to_htmlnode(markdown)
        expected = ParentNode('div', [ParentNode('pre', [LeafNode("code", 'code')])])
        self.assertEqual(result, expected)

    def test_quote(self):
        markdown = "> This is a quote\n> This is also a quote"
        result = markdown_to_htmlnode(markdown)
        expected = ParentNode('div', [ParentNode('blockquote', [
            ParentNode('p', text_to_children("This is a quote")),
            ParentNode('p', text_to_children("This is also a quote"))
        ])])
        self.assertEqual(result, expected)

    def test_unordered_list(self):
        markdown = "* Item 1\n* Item 2"
        result = markdown_to_htmlnode(markdown)
        expected = ParentNode('div', [ParentNode('ul', [
            ParentNode('li', text_to_children("Item 1")),
            ParentNode('li', text_to_children("Item 2"))
        ])])
        self.assertEqual(result, expected)

    def test_ordered_list(self):
        markdown = "1. Item 1\n2. Item 2"
        result = markdown_to_htmlnode(markdown)
        expected = ParentNode('div', [ParentNode('ol', [
            ParentNode('li', text_to_children("Item 1")),
            ParentNode('li', text_to_children("Item 2"))
        ])])
        self.assertEqual(result, expected)

    def test_paragraph(self):
        markdown = "This is a paragraph."
        result = markdown_to_htmlnode(markdown)
        expected = ParentNode('div', [ParentNode('p', text_to_children("This is a paragraph."))])
        self.assertEqual(result, expected)

    def test_mixed_markdown(self):
        markdown = """
# Heading 1

## Heading 2

### Heading 3

This is a paragraph with some **bold text** and _italictext_.

* Unordered list item 1
* Unordered list item 2

1. Ordered list item 1
2. Ordered list item 2

> This is a quote.
> This is part of the same quote.

```
code block
with multiple lines
```

Another paragraph.

## Another Heading 2

```
another code block
```

> Another quote.
                """

        result = markdown_to_htmlnode(markdown)

        expected = ParentNode('div', [
            ParentNode('h1', text_to_children("Heading 1")),
            ParentNode('h2', text_to_children("Heading 2")),
            ParentNode('h3', text_to_children("Heading 3")),
            ParentNode('p', text_to_children(
                "This is a paragraph with some **bold text** and _italictext_."
            )),
            ParentNode('ul', [
                ParentNode('li', text_to_children("Unordered list item 1")),
                ParentNode('li', text_to_children("Unordered list item 2"))
            ]),
            ParentNode('ol', [
                ParentNode('li', text_to_children("Ordered list item 1")),
                ParentNode('li', text_to_children("Ordered list item 2"))
            ]),
            ParentNode('blockquote', [
                ParentNode('p', text_to_children("This is a quote.")),
                ParentNode('p', text_to_children(
                    "This is part of the same quote."))
            ]),
            ParentNode(
                'pre', [
                    LeafNode("\ncode block\nwith multiple lines\n", 'code')
                ]),
            ParentNode('p', text_to_children("Another paragraph.")),
            ParentNode('h2', text_to_children("Another Heading 2")),
            ParentNode('pre', [LeafNode("\nanother code block\n", 'code')]),
            ParentNode('blockquote', [
                ParentNode('p', text_to_children("Another quote."))
            ]),
        ])
        self.maxDiff = None
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
