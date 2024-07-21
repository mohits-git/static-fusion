import unittest
from app.leafnode import LeafNode
from app.textnode_to_htmlnode import text_node_to_html_node
from app.textnode import TextNode


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        textnode = TextNode('hello mofos', 'text')
        htmlnode = text_node_to_html_node(textnode)
        expected_htmlnode = LeafNode('hello mofos')
        self.assertEqual(htmlnode, expected_htmlnode,
                         "TextNode to HTMLNode conversion test failed")

    def test_bold(self):
        textnode = TextNode('hello mofos', 'bold')
        htmlnode = text_node_to_html_node(textnode)
        expected_htmlnode = LeafNode('hello mofos', 'b')
        self.assertEqual(htmlnode, expected_htmlnode,
                         "TextNode to HTMLNode conversion test failed")

    def test_italic(self):
        textnode = TextNode('hello mofos', 'italic')
        htmlnode = text_node_to_html_node(textnode)
        expected_htmlnode = LeafNode('hello mofos', 'i')
        self.assertEqual(htmlnode, expected_htmlnode,
                         "TextNode to HTMLNode conversion test failed")

    def test_code(self):
        textnode = TextNode('hello mofos', 'code')
        htmlnode = text_node_to_html_node(textnode)
        expected_htmlnode = LeafNode('hello mofos', 'code')
        self.assertEqual(htmlnode, expected_htmlnode,
                         "TextNode to HTMLNode conversion test failed")

    def test_link(self):
        textnode = TextNode('hello mofos', 'link', 'http://localhost:3000')
        htmlnode = text_node_to_html_node(textnode)
        expected_htmlnode = LeafNode('hello mofos', 'a', {
            "href": 'http://localhost:3000'
        })
        self.assertEqual(htmlnode, expected_htmlnode,
                         "TextNode to HTMLNode conversion test failed")

    def test_image(self):
        textnode = TextNode("A dog image", 'image', 'public/dog.png')
        htmlnode = text_node_to_html_node(textnode)
        expected_htmlnode = LeafNode(None, 'img', {
            'src': 'public/dog.png',
            'alt': 'A dog image',
        })
        self.assertEqual(htmlnode, expected_htmlnode,
                         "TextNode to HTMLNode conversion test failed")


if __name__ == "__main__":
    unittest.main()
