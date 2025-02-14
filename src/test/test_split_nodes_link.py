import unittest
from app.split_textnodes import split_nodes_link
from app.textnode import TextNode
from app.custom_types import text_type


class TestSplitNodesLink(unittest.TestCase):
    def test_markdown_links(self):
        old_nodes = [
            TextNode(
                "hello this is my [portfolio](https://www.mohits.site)",
                text_type.text.name
            )
        ]
        new_nodes = split_nodes_link(old_nodes)
        expected_nodes = [
            TextNode("hello this is my ", text_type.text.name),
            TextNode("portfolio", text_type.link.name,
                     "https://www.mohits.site"),
        ]
        self.assertEqual(new_nodes, expected_nodes,
                         "Split Nodes Links Test failed")

    def test_markdown_multiple_links(self):
        old_nodes = [
            TextNode(
                "hello this is my [portfolio](https://www.mohits.site)",
                text_type.text.name
            ),
            TextNode(
                "hello this is my [portfolio](https://www.mohits.site) and this is my [twitter](https://www.x.com/mohits_twt)",
                text_type.text.name
            )
        ]
        new_nodes = split_nodes_link(old_nodes)
        expected_nodes = [
            TextNode("hello this is my ", text_type.text.name),
            TextNode("portfolio", text_type.link.name,
                     "https://www.mohits.site"),
            TextNode("hello this is my ", text_type.text.name),
            TextNode("portfolio", text_type.link.name,
                     "https://www.mohits.site"),
            TextNode(" and this is my ", text_type.text.name),
            TextNode("twitter", text_type.link.name,
                     "https://www.x.com/mohits_twt")
        ]
        self.assertEqual(new_nodes, expected_nodes,
                         "Split Nodes Links Test failed")
