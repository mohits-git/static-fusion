import unittest
from app.split_textnodes import split_nodes_link
from app.textnode import TextNode


text_type_text = "text"
text_type_link = "link"


class TestSplitNodesLink(unittest.TestCase):
    def test_markdown_links(self):
        old_nodes = [
            TextNode(
                "hello this is my [portfolio](https://www.mohits.site)",
                text_type_text
            )
        ]
        new_nodes = split_nodes_link(old_nodes)
        expected_nodes = [
            TextNode("hello this is my ", text_type_text),
            TextNode("portfolio", text_type_link, "https://www.mohits.site"),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_markdown_multiple_links(self):
        old_nodes = [
            TextNode(
                "hello this is my [portfolio](https://www.mohits.site)",
                text_type_text
            ),
            TextNode(
                "hello this is my [portfolio](https://www.mohits.site) and this is my [twitter](https://www.x.com/mohits_twt)",
                text_type_text
            )
        ]
        new_nodes = split_nodes_link(old_nodes)
        expected_nodes = [
            TextNode("hello this is my ", text_type_text),
            TextNode("portfolio", text_type_link, "https://www.mohits.site"),
            TextNode("hello this is my ", text_type_text),
            TextNode("portfolio", text_type_link, "https://www.mohits.site"),
            TextNode(" and this is my ", text_type_text),
            TextNode("twitter", text_type_link, "https://www.x.com/mohits_twt")
        ]
        self.assertEqual(new_nodes, expected_nodes)
