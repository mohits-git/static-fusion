import unittest

from app.text_to_textnodes import text_to_textnodes
from app.text_type import text_type
from app.textnode import TextNode


class TestTextToTextNodes(unittest.TestCase):
    def test_markdown_line(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        textnodes = text_to_textnodes(text)
        expected_textnodes = [
            TextNode("This is ", text_type.text.name),
            TextNode("text", text_type.bold.name),
            TextNode(" with an ", text_type.text.name),
            TextNode("italic", text_type.italic.name),
            TextNode(" word and a ", text_type.text.name),
            TextNode("code block", text_type.code.name),
            TextNode(" and an ", text_type.text.name),
            TextNode("obi wan image", text_type.image.name,
                     "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", text_type.text.name),
            TextNode("link", text_type.link.name, "https://boot.dev"),
        ]
        self.maxDiff = None
        self.assertEqual(
            textnodes,
            expected_textnodes,
            "Failed at text to textnodes conversion test"
        )

    def test_markdown_complex_line(self):
        text = "This is **text** with an *italic* and the **bold** word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) *italic* **bold** `code`"
        textnodes = text_to_textnodes(text)
        expected_textnodes = [
            TextNode("This is ", text_type.text.name),
            TextNode("text", text_type.bold.name),
            TextNode(" with an ", text_type.text.name),
            TextNode("italic", text_type.italic.name),
            TextNode(" and the ", text_type.text.name),
            TextNode("bold", text_type.bold.name),
            TextNode(" word and a ", text_type.text.name),
            TextNode("code block", text_type.code.name),
            TextNode(" and an ", text_type.text.name),
            TextNode("obi wan image", text_type.image.name,
                     "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", text_type.text.name),
            TextNode("link", text_type.link.name, "https://boot.dev"),
            TextNode(" ", text_type.text.name),
            TextNode("italic", text_type.italic.name),
            TextNode(" ", text_type.text.name),
            TextNode("bold", text_type.bold.name),
            TextNode(" ", text_type.text.name),
            TextNode("code", text_type.code.name),
        ]
        self.maxDiff = None
        self.assertEqual(
            textnodes,
            expected_textnodes,
            "Failed at text to textnodes conversion test"
        )
