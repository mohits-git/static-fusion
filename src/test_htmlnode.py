import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        props = {
            "class": "text-2xl"
        }
        children = []
        node1 = HTMLNode("p", "this is a paragraph", children, props)
        node2 = HTMLNode("p", "this is a paragraph", children, props)
        self.assertEqual(node1, node2)

    def test_noteq(self):
        node1 = HTMLNode("p", "this is a paragraph", None, {
            "class": "text-2xl"
        })
        node2 = HTMLNode("a", "this is a anchor tag", None, {
            "href": "http://localhost:3000",
            "class": "text-2xl"
        })
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node1 = HTMLNode("p", "this is a paragraph", None, {
            "class": "text-2xl"
        })
        node2 = HTMLNode("a", "this is a anchor tag", None, {
            "href": "http://localhost:3000",
            "class": "text-2xl"
        })
        print('-------------TEST HTMLNode - [__repr__()]------------------')
        print(node1.__repr__())
        print(node2.__repr__())
        print('--------------------------------------------------------------')

    def test_withchildren(self):
        node1 = HTMLNode("p", "this is a paragraph", None, {
            "class": "text-2xl"
        })
        node2 = HTMLNode("a", "this is a anchor tag", None, {
            "href": "http://localhost:3000",
            "class": "text-2xl"
        })
        node3 = HTMLNode("div", None, [node1, node2], {
            "class": "flex items-center justify-center"
        })
        print('-------------TEST HTMLNode - [With Children]------------------')
        print(node3.__repr__())
        print('--------------------------------------------------------------')
