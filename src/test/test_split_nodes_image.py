import unittest
from app.split_textnodes import split_nodes_image
from app.textnode import TextNode


text_type_text = "text"
text_type_image = "image"


class TestSplitNodesLink(unittest.TestCase):
    def test_markdown_images(self):
        old_nodes = [
            TextNode(
                "hello this is my ![portfolio](https://www.mohits.site)",
                text_type_text
            )
        ]
        new_nodes = split_nodes_image(old_nodes)
        expected_nodes = [
            TextNode("hello this is my ", text_type_text),
            TextNode("portfolio", text_type_image, "https://www.mohits.site"),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_markdown_multiple_images(self):
        old_nodes = [
            TextNode(
                "hello this is my ![portfolio](https://www.mohits.site)",
                text_type_text
            ),
            TextNode(
                "hello this is my ![portfolio](https://www.mohits.site) and this is my ![twitter](https://www.x.com/mohits_twt)",
                text_type_text
            )
        ]
        new_nodes = split_nodes_image(old_nodes)
        expected_nodes = [
            TextNode("hello this is my ", text_type_text),
            TextNode("portfolio", text_type_image, "https://www.mohits.site"),
            TextNode("hello this is my ", text_type_text),
            TextNode("portfolio", text_type_image, "https://www.mohits.site"),
            TextNode(" and this is my ", text_type_text),
            TextNode("twitter", text_type_image, "https://www.x.com/mohits_twt")
        ]
        self.assertEqual(new_nodes, expected_nodes)
