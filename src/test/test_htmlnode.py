import unittest
from app.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        props = {
            "class": "text-2xl"
        }
        children = []
        node1 = HTMLNode("p", "this is a paragraph", children, props)
        node2 = HTMLNode("p", "this is a paragraph", children, props)
        self.assertEqual(node1, node2, "HTMLNode test failed")

    def test_noteq(self):
        node1 = HTMLNode("p", "this is a paragraph", None, {
            "class": "text-2xl"
        })
        node2 = HTMLNode("a", "this is a anchor tag", None, {
            "href": "http://localhost:3000",
            "class": "text-2xl"
        })
        self.assertNotEqual(node1, node2, "HTMLNode test failed")

    def test_repr(self):
        node1 = HTMLNode("p", "this is a paragraph", None, {
            "class": "text-2xl"
        })
        node2 = HTMLNode("a", "this is a anchor tag", None, {
            "href": "http://localhost:3000",
            "class": "text-2xl"
        })
        expected_node1_repr = '<p class="text-2xl">this is a paragraph</p>'
        expected_node2_repr = '<a href="http://localhost:3000" class="text-2xl">this is a anchor tag</a>'
        self.assertEqual(node1.__repr__(), expected_node1_repr,
                         "HTMLNode test failed")
        self.assertEqual(node2.__repr__(), expected_node2_repr,
                         "HTMLNode test failed")

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
        expected_str = '<div class="flex items-center justify-center">\n<p class="text-2xl">this is a paragraph</p>\n<a href="http://localhost:3000" class="text-2xl">this is a anchor tag</a>\n</div>'
        self.assertEqual(node3.__repr__(), expected_str,
                         "HTMLNode test failed")


if __name__ == "__main__":
    unittest.main()
